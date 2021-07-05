# Setup Instructions #

- Add python to your PATH environment if necessary
- Put geckodriver in your system's PATH location or add geckodriver to PATH directly
- Update "sample_creds.json" to contain your credentaisl and rename to "creds.json"

# Windows Scheduler Instructions: #

Actions:
- Program/script = <path_to_this_repository>/start_rigging.cmd
- Start in = <path_to_this_repository>
- Set trigger to your desired time interval
- Firefox is not headless, you will see a pop-up when it runs
