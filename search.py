import os
import subprocess
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.helpers import escape_markdown
import psutil
import asyncio
from concurrent.futures import ProcessPoolExecutor

# Replace with your actual bot API token
BOT_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
USER_ID = XXXXXXXX

# Telegram message length limit
MAX_MESSAGE_LENGTH = 4096

# Function to get CPU model
def get_cpu_info():
    return f"{psutil.cpu_count(logical=False)} Cores, {psutil.cpu_freq().current:.2f}MHz"

def split_long_message(message, max_length=MAX_MESSAGE_LENGTH):
    """Split a long message into smaller chunks within the max length limit."""
    return [message[i:i + max_length] for i in range(0, len(message), max_length)]

def search_database(search_keyword, database_folder, output_file_path):
    """Run the search command in a separate process."""
    subprocess.run([
        "C:\\Forensic Files (x64)\\AgentRansack\\AgentRansack.exe",  # Adjust path if necessary
        "-d", database_folder,
        "-c", search_keyword,
        "-o", output_file_path,
        "-s"
    ])

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a search keyword, e.g., /search ABCD")
        return

    search_keyword = ' '.join(context.args)
    cpu_info = get_cpu_info()
    
    verbose_mode = '--verbose' in context.args  # Enable verbose mode if specified
    if verbose_mode:
        await update.message.reply_text(f"Verbose Mode Enabled\nCPU: `{cpu_info}`\nSearching for: `{escape_markdown(search_keyword)}`...")
    else:
        await update.message.reply_text(f"CPU: {cpu_info}\nSearching for: {escape_markdown(search_keyword)}...")

    try:
        database_folder = "C:\\Users\\Administrator\\Desktop\\Database"  # Change to your database folder
        output_file_path = "C:\\Users\\Administrator\\Desktop\\search_results.txt"  # Change to your output file path

        total_file_count = sum(len(files) for _, _, files in os.walk(database_folder))
        progress_message = await update.message.reply_text(f"Total Files in Database: `{total_file_count}`")

        # Use ProcessPoolExecutor to utilize full CPU power
        with ProcessPoolExecutor() as executor:
            future = executor.submit(search_database, search_keyword, database_folder, output_file_path)

            start_time = time.time()
            files_processed = 0
            chunk_size = total_file_count // 100 if total_file_count > 100 else 1

            while not future.done():
                await asyncio.sleep(1)

                files_processed += chunk_size
                if files_processed > total_file_count:
                    files_processed = total_file_count

                current_time = time.time()
                progress_percentage = (files_processed * 100) // total_file_count
                elapsed_time = time.time() - start_time
                elapsed_time_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

                remaining_files = total_file_count - files_processed
                speed = files_processed / elapsed_time if elapsed_time > 0 else 0
                remaining_time = remaining_files / speed if speed > 0 else float('inf')
                remaining_time_str = time.strftime("%H:%M:%S", time.gmtime(remaining_time))

                progress_bar_length = 20
                filled_length = int(progress_bar_length * progress_percentage // 100)
                bar = '█' * filled_length + '-' * (progress_bar_length - filled_length)

                progress_message_text = (
                    f"{progress_percentage:3d}%|{bar}| {files_processed}/{total_file_count}` "
                    f"[{elapsed_time_str}<{remaining_time_str}, {speed:.2f} files/s]"
                )

                try:
                    await progress_message.edit_text(progress_message_text)  # Edit the same progress message
                except Exception as e:
                    print(f"Error updating progress message: {e}")

            # Wait for the process to complete
            future.result()  # This will raise an error if the subprocess failed

        if os.path.exists(output_file_path):
            try:
                with open(output_file_path, "r", encoding='utf-8') as f:
                    search_results = f.read()
            except UnicodeDecodeError:
                with open(output_file_path, "r", encoding='latin1') as f:
                    search_results = f.read()

            if search_results.strip():
                if verbose_mode:
                    await update.message.reply_text("Search Results:\n```\n" + search_results + "\n```")  # Using triple backticks for code block
                else:
                    result_chunks = split_long_message(search_results)
                    for chunk in result_chunks:
                        await update.message.reply_text(chunk)
            else:
                await update.message.reply_text("No results found or an error occurred.")
        else:
            await update.message.reply_text("Output file not found.")

    except Exception as e:
        await update.message.reply_text(f"Error occurred: `{str(e)}`")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("search", search_command))
    application.add_error_handler(error_handler)

    try:
        application.run_polling()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == '__main__':
    main()
