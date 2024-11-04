# import os
# import logging
# from datetime import datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
# from git import Repo, GitCommandError

# # Configure logging to log errors and information
# logging.basicConfig(
#     filename='git_automation.log',
#     level=logging.INFO,
#     format='%(asctime)s:%(levelname)s:%(message)s'
# )

# # Define the path to the local Git repository
# REPO_PATH = '/home/frusher/Desktop/LLMProject'

# def git_pull():
#     """Performs 'git pull' to sync the repository with the remote."""
#     try:
#         repo = Repo(REPO_PATH)
#         origin = repo.remotes.origin
#         origin.pull()
#         logging.info("Git pull successful.")
#     except GitCommandError as e:
#         logging.error(f"Git pull failed: {e}")
#     except Exception as e:
#         logging.error(f"An unexpected error occurred during git pull: {e}")

# def git_add_commit_push():
#     """Adds all changes, commits them, and pushes to the remote repository."""
#     try:
#         repo = Repo(REPO_PATH)
#         repo.git.add(all=True)
#         commit_message = f"Automated backup commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#         repo.index.commit(commit_message)
#         origin = repo.remotes.origin
#         origin.push()
#         logging.info("Git add, commit, and push successful.")
#     except GitCommandError as e:
#         logging.error(f"Git commit/push failed: {e}")
#     except Exception as e:
#         logging.error(f"An unexpected error occurred during git commit/push: {e}")

# # def main():
# #     """Schedules the git tasks and starts the scheduler."""
# #     scheduler = BlockingScheduler()
# #     # Schedule git_pull every day at 7:00 AM
# #     scheduler.add_job(git_pull, 'cron', hour=7, minute=0)
# #     # Schedule git_add_commit_push every day at 7:00 PM
# #     scheduler.add_job(git_add_commit_push, 'cron', hour=19, minute=0)
# #     try:
# #         logging.info("Scheduler started.")
# #         scheduler.start()
# #     except (KeyboardInterrupt, SystemExit):
# #         logging.info("Scheduler stopped.")



# # REPO_PATH = '/home/frusher/Desktop/LLMProject'
# def main():
#     """Schedules the git tasks and starts the scheduler."""
#     scheduler = BlockingScheduler()
#     # Run git_pull every 10 seconds (for testing purposes)
#     scheduler.add_job(git_pull, 'interval', seconds=10)
#     # Run git_add_commit_push every 15 seconds (for testing purposes)
#     scheduler.add_job(git_add_commit_push, 'interval', seconds=15)
#     try:
#         logging.info("Scheduler started.")
#         scheduler.start()
#     except (KeyboardInterrupt, SystemExit):
#         logging.info("Scheduler stopped.")


# if __name__ == "__main__":
#     main()

import schedule
import time
import logging
from git import Repo, GitCommandError
import os

# Configure logging
logging.basicConfig(filename='git_automation.log', level=logging.ERROR)

# Set the path to the repository
repo_path = '/home/frusher/Desktop/LLMProject'

def git_pull():
    try:
        # Change the working directory to the repository path
        os.chdir(repo_path)
        # Initialize the repo object
        repo = Repo(repo_path)
        # Perform a git pull
        repo.remotes.origin.pull()
        logging.info("Git pull successful.")
    except GitCommandError as gce:
        logging.error(f"Git pull failed: {gce}")
    except Exception as e:
        logging.error(f"Error during git pull: {e}")

def git_push():
    try:
        # Change the working directory to the repository path
        os.chdir(repo_path)
        # Initialize the repo object
        repo = Repo(repo_path)
        # Perform git add, commit, and push
        repo.git.add(A=True)
        repo.git.commit(m='Automated backup commit')
        repo.remotes.origin.push()
        logging.info("Git push successful.")
    except GitCommandError as gce:
        logging.error(f"Git push failed: {gce}")
    except Exception as e:
        logging.error(f"Error during git push: {e}")

# Schedule the git pull every morning at 7:00 AM
# schedule.every().day.at("07:00").do(git_pull)
schedule.every(10).seconds.do(git_pull)


# Schedule the git push every evening at 7:00 PM
# schedule.every().day.at("19:00").do(git_push)
schedule.every(10).seconds.do(git_push)


# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)