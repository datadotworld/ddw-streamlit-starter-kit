# Streamlit Starter Kit for data.world's AI Context Engine

This starter kit will let you quickly get started with data.world's AI Context Engine™. It is a simple Streamlit app that demonstrates how to use the data.world API to send a question to the AI Context Engine and display its response.

## Getting started

### Pre-requisites

- Python v3.12 or later
- [Poetry](https://python-poetry.org/) v1.8.3 or later
- A [data.world](https://data.world) account, with an AI Context Engine™ License and available Knowledge Tokens

### Installation

First, fetch this repo however you like:

- Clone it using the web URL

  ```sh
  git clone https://github.com/datadotworld/ddw-streamlit-starter-kit.git
  ```

or

- Use the GitHub CLI

  ```sh
  gh repo clone datadotworld/ddw-streamlit-starter-kit
  ```

or

- Download it via this link [ddw-streamlit-starter-kit.zip](https://github.com/datadotworld/ddw-streamlit-starter-kit/archive/refs/heads/main.zip) and unzip it.


Then, navigate to the project directory:

```sh
$ cd ddw-streamlit-starter-kit
```

Get a data.world token (either as [an individual user](https://developer.data.world/docs/api-keys-and-auth#method-2-acquiring-tokens-via-the-ui) for development, or from a [service account](https://docs.data.world/en/130574-creating-and-managing-service-accounts.html) for deployment), copy `secrets.toml.example` to `.streamlit/secrets.toml`, replacing the placeholder token:

```toml
[ddw]
api_endpoint = "https://api.data.world"
token = "apikey123"
```

In the vast majority of most cases, you'll be able to leave the default `api_endpoint` value as is.

### Running the app

There are a multitude of ways to set up a Python virtual environment. Here, we will use Poetry. From the root of the project you cloned or downloaded:

```sh
$ poetry --version # Ensure you have a recent version of Poetry installed
$ poetry install   # Installs both production dependencies and development dependencies
$ poetry shell     # Activates the virtual environment
```

Then, you may start the app:

```sh
$ streamlit run app.py
```

This will open a new tab in your default browser with the app running. You'll see two form fields for specifying your organization ID, project ID, and a text field for entering a question. After entering the required information, click the "Get Answer" button to send the question to the AI Context Engine. The response will be displayed below the form. All of this is driven by Streamlit and the `app.py` script.

### Developing the app

We make use of standard tools in the Python ecosystem for development. We use `black` for code formatting, `flake8` for linting, and `isort` for organizing imports:

```sh
# Activate the virtual environment if you haven't already: poetry shell
$ black .
$ flake8 .
$ isort .
```

#### Testing

After setting up a `secrets.toml` file as described above, you can run the tests:

```sh
# Activate the virtual environment if you haven't already: poetry shell
$ pytest
```

### Deploying the app

Since this is Streamlit, the easiest way to deploy the app is to use Streamlit's own hosting service. You can find more information in their documentation, ["Deploy your app"](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

## Contributing

We welcome contributions to this project. Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more information.
