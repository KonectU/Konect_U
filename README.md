
# Konectu Telemetry Data Collection 📈

## Overview

At Konectu, we aim to build a dataset that can be used by the AI community to develop better Large Action Models (LAMs) for improving Web Agents. These datasets help refine and create more intelligent web automation tools. You can find our ongoing work on the [BigAction HuggingFace page](https://huggingface.co/BigAction).

This README outlines the data we collect from users, how it contributes to our mission, and the potential consequences of this data collection.

## Data Collected by Konectu

To create a robust and useful dataset, Konectu collects the following telemetry data by default:

- **Version of Konectu installed**: The version of the software being used.
- **Code / List of actions generated for each web action step**: The actions performed by the agent in interacting with web pages.
- **The past actions**: A history of previous actions taken during a session.
- **The "observations"**: The method used to check the current state of the webpage (e.g., DOM analysis).
- **LLM used**: The type of language model utilized (e.g., GPT-4).
- **Multi-modal LLM used**: If a multi-modal model is used (e.g., GPT-4 multimodal), this will be recorded.
- **Randomly generated anonymous user ID**: A unique, non-identifiable ID is assigned to each user session.
- **Interface type**: Whether you are using a CLI command (`konectu-qa` for example), the Gradio demo, or our library directly.
- **The objective used**: The task or objective the agent is working towards (e.g., form submission, data extraction).
- **The chain of thoughts on the agent**: The reasoning process behind the agent’s decisions (also known as chain-of-thoughts).
- **The interaction zone on the page**: The specific area on the webpage the agent interacted with (bounding box).
- **The viewport size of your browser**: The dimensions of the user's browser window.
- **The current step**: The specific step the agent is performing in the task sequence.
- **The instruction(s) generated & the current engine used**: The generated instructions and the engine currently driving the interaction.
- **Token costs & usages**: Data related to token consumption, which includes cost and usage metrics.

## Consequences of Data Collection

### Positive Consequences

1. **Advancement of AI Development**: By collecting this data, we are contributing to the development of Large Action Models (LAMs) that can automate complex web interactions more effectively.
2. **Improved Web Agents**: These datasets will help improve the accuracy and intelligence of Web Agents, leading to more capable and efficient systems.
3. **Collaborative AI Research**: By sharing this data on platforms like HuggingFace, we foster an environment of open collaboration with the AI community, accelerating progress in AI model development.
4. **Personalization & User Experience**: Understanding user actions and objectives helps improve and personalize user interactions with Konectu.



## Data Usage & Privacy

We strive to balance the need for data to improve our models with the privacy and security concerns of our users. The data collected is used **solely for the purpose of improving Web Agents and Large Action Models**, and it is shared with the AI community only in a manner that respects user anonymity.

### Key Principles

- **Anonymization**: We ensure all data is tied to a randomly generated anonymous user ID.
- **Transparency**: Users are informed about what data is collected and how it is used.
- **Data Minimization**: We only collect the data necessary to improve Web Agents and LAMs.
- **Security**: All collected data is stored securely and handled with strict security protocols.

## Opt-Out

Currently, data collection is enabled by default, but we are working on mechanisms that allow users to **opt out** of data collection. Stay tuned for updates on this.

## Getting Started 🚀

To get started with Konectu, check out our documentation and usage guides. Once you have installed Konectu, telemetry data will be collected as outlined above, contributing to the improvement of AI systems.

For more information, visit our [BigAction HuggingFace page](https://huggingface.co/BigAction).

---

Thank you for contributing to the advancement of AI and Web Agents! Your interactions with Konectu help us build better systems for everyone.

## License

Konectu is open-source software. See the [LICENSE](LICENSE) file for more information.
