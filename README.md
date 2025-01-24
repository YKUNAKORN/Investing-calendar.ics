# ICS Calendar Hosting with GitHub Pages

This project provides a simple solution to host `.ics` calendar files using GitHub Pages, enabling public sharing and subscription via `webcal://` links. The goal is to make calendar events accessible and automatically updatable for applications like iPhone Calendar or iCalendar.

## Features
- **Free Hosting**: Utilize GitHub Pages for free, reliable hosting of `.ics` files.
- **Cross-Platform Support**: Share calendars for iOS, macOS, and other devices that support `webcal://`.
- **Automatic Updates**: Any changes to the `.ics` file will automatically reflect on subscribed devices.

## Getting Started

### Step 1: Create a Repository
1. Log in to your GitHub account.
2. Create a new public repository (e.g., `ics-calendar`).

### Step 2: Upload the `.ics` File
1. Click on the **"Add file"** button in the repository and choose **"Upload files"**.
2. Drag and drop your `.ics` file or use the **"Choose your files"** button to upload.
3. Commit the changes by clicking **"Commit changes"**.

### Step 3: Enable GitHub Pages
1. Go to the **Settings** tab of your repository.
2. Scroll down to **Pages** under the **"Code and automation"** section.
3. In the **"Branch"** dropdown, select `main` and set the folder to `/root`.
4. Click **"Save"** to enable GitHub Pages.

### Step 4: Generate the `webcal://` Link
1. The GitHub Pages URL for your `.ics` file will look like this:
   ```
   https://USERNAME.github.io/REPOSITORY_NAME/filename.ics
   ```
2. Convert the `https://` URL to `webcal://`:
   ```
   webcal://USERNAME.github.io/REPOSITORY_NAME/filename.ics
   ```

### Step 5: Share and Subscribe
- Share the `webcal://` link with users.
- On iPhone or macOS, users can subscribe to the calendar by pasting the link into the subscription calendar feature.

## Example
- Original GitHub Pages Link:
  ```
  https://yourusername.github.io/ics-calendar/events.ics
  ```
- Webcal Link:
  ```
  webcal://yourusername.github.io/ics-calendar/events.ics
  ```

## Notes
- Ensure the `.ics` file is correctly formatted to avoid validation issues.
- Any updates to the `.ics` file in the repository will automatically propagate to subscribed users.

## License
This project is open-source and available under the [MIT License](LICENSE).# ics-calendar
