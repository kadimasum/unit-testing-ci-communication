# Unit Testing, CI, and Communication

Welcome to the "Unit Testing, CI, and Communication" repository. This project illustrates writing unit tests for a simple Python application, automating tests using GitHub Actions, and integrating Slack for effective communication.

## Table Of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Unit Testing](#unit-testing)
- [Continuous Integration (CI)](#continuous-integration-ci)
- [Communication with Slack](#communication-with-slack)

## Prerequisites
Before you begin, make sure you have the following prerequisites:

- Basic Python programming knowledge
- Familiarity with version control (Git & GitHub)
- Slack installed on your device

## Getting Started
1. Clone the repository to your local machine:

    - Clone with SSH

   ```bash
   git clone git@github.com:kadimasum/unit-testing-ci-communication.git
   ```

   - Clone with HTTPS

   ```bash
   git clone https://github.com/kadimasum/unit-testing-ci-communication.git
   ```
   

2. Change to the project directory:

   ```bash
   cd unit-testing-ci-communication
   ```


## Unit Testing
Explore the `phonebook.py` file to understand the basic structure of the Phonebook class. The `phonebook_test.py` file contains unit tests for this class. To run the tests locally:

```bash
python3 phonebook_test.py
```

## Continuous Integration (CI)
The project is configured with GitHub Actions for automated testing on every push and pull request. The workflow is defined in the [`.github/workflows/ci.yml`](.github/workflows/ci.yml) file. It includes steps to:
- Check out the code
- Set up the Python environment
- Run the unit tests
- Notify on Slack for both success and failure scenarios


## Communication with Slack
To receive notifications on Slack, follow these steps:

1. Set up a Slack Incoming Webhook. Refer to the [Slack documentation](https://github.com/marketplace/actions/slack-notify) for instructions.
   
2. Add the Slack Webhook as a secret in your GitHub repository:
   - Go to "Settings" -> "Secrets" -> "New repository secret"
   - Name: `SLACK_WEBHOOK`
   - Value: [Your Slack Webhook URL]

Now, when the CI workflow runs, it will send notifications to the configured Slack channel.



## Contributing
We encourage contributions! If you have suggestions, enhancements, or bug fixes, please [open an issue](https://github.com/kadimasum/unit-testing-ci-communication/issues) or submit a pull request.


## License
This project is licensed under the [MIT License](./LICENSE).

