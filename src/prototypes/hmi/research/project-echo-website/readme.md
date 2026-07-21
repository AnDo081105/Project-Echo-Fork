# Project Echo Prototype Website

Owner: HMI team
Status: Standalone awareness website prototype; not production HMI runtime

This folder was moved to HMI research from `src/prototypes/R and D/Project Echo Website` after checking that no generated dependency output such as `node_modules` was present. It is separate from the production dashboard at `src/production/HMI/ui`.

## Reorganisation Notes

- Runtime entry point: `server.js`.
- Static pages and images live under `src/`.
- Local run command serves the prototype on `localhost:3000`.
- `package.json` currently runs `npm install` as `prestart`; keep generated dependencies out of Git.
- The pages use external CDN/font/social/video URLs, for example `src/index.html:9`, `src/index.html:11`, `src/index.html:14`, `src/vision.html:48`, and `src/vision.html:62-65`.
- Keep this folder visible as HMI-owned prototype work until archive or promotion is approved.

# Node.js and Nodemon Documentation

## Node.js

**Node.js** is an open-source, cross-platform, JavaScript runtime environment that executes JavaScript code outside of a web browser. It allows developers to use JavaScript to write command line tools and for server-side scripting—running scripts server-side to produce dynamic web page content before the page is sent to the user's web browser.

## Nodemon

**Nodemon** is a utility that will monitor for any changes in your source and automatically restart your server. It's perfect for development. Install it using `npm install -g nodemon`. Then you can just use `nodemon app.js` to run your application, and it will automatically restart when a file changes.

## Prestart in package.json

In `package.json`, you can specify scripts that can be run with the `npm run` command. The `prestart` script is a special script that runs automatically before the `start` script. This can be useful for setting up the environment or performing other necessary preconditions before starting your application.

## Running the project on a local server

In the **terminal** opened in the project echo directory, use `cd src/prototypes/hmi/research/project-echo-website` to access the files of the Project Echo awareness website. Further, running the `npm run start` command in that terminal will install all the Node.js dependencies automatically, while also hosting it on **localhost:3000**. Changes made to files except `server.js` will be reflected without **restarting the npm run start script**.
