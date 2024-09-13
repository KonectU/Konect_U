

## Konectu 

Konectu is an open-source framework designed for developers who want to create AI Web Agents to automate processes for their end users.

Our Web Agents can take an objective, such as "Print installation steps for Hugging Face's Diffusers library," and generate and perform the actions required to achieve the objective.

Konectu Agents are made up of:

- A World Model that takes an objective and the current state (aka the current web page) and outputs an appropriate set of instructions.
- An Action Engine which “compiles” these instructions into action code, e.g., Selenium or Playwright & executes them


### Konectu QA: Dedicated tooling for QA Engineers
**🌊 Built on Konectu**

Konectu QA is a tool tailored for QA engineers leveraging our framework. 

It allows you to automate test writing by turning Gherkin specs into easy-to-integrate tests. Konectu QA is a project leveraging the Konectu framework behind the scenes to make web testing 10x more efficient.

## Key Features

- ✅ [Built-in Contexts]
- ✅ [Customizable configuration]
- ✅ [A test runner]
- ✅ A [Token Counter]
- ✅ [Logging tools]
- ✅ [Gradio interface]
- ✅ [Debugging tools]
- ✅ [A Chrome Extension]


## Key Benefits

* Faster test creation: generate Pytest code directly from test scenarios by leveraging LaVague Agents.
* Reduced maintenance: AI element selection adapts to UI changes, lowering the upkeeping needed when the site changes.

## Installation
Installing the latest release
You can install the latest release of Konectu with the following command:

'''bash pip install konectu

This will install a core bundle of Konectu packages required for usage of Konectu with default configurations - you can see which packages are included in this bundle in out pyproject.toml file at the root of our repo.

Optional Konectu packages

If you want to use packages not included in our default bundle, you will need to manually install the relevant package.

For example, if you want to use a non-default context such as the Gemini context. You would need to run:


'''bash
 pip install Konectu.contexts.gemini 
 

## Installing from source
If you want to install from source, you can do so by cloning the repo and running the following command from the root of the repo:


'''bash
 pip install -e .



## 📈 Data collection

We want to build a dataset that can be used by the AI community to build better Large Action Models for better Web Agents. 

This is why Konectu collects the following user data telemetry by default:

- Version of Konectu installed
- Code / List of actions generated for each web action step
- The past actions
- The "observations" (method used to check the current page)
- LLM used (i.e GPT4)
- Multi modal LLM used (i.e GPT4)
- Randomly generated anonymous user ID
- Whether you are using a CLI command (Konectu-qa for example), the Gradio demo or our library directly.
- The objective used 
- The chain of thoughts on the agent
- The interaction zone on the page (bounding box)
- The viewport size of your browser
- The current step
- The instruction(s) generated & the current engine used
- The token costs & usages
- The URL you performed an action on
- Whether the action failed or succeeded
- The extra used data specified
- Error message, where relevant
- The source nodes (chunks of HTML code retrieved from the web page to perform this action)

