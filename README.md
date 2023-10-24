# Amazon HackOn

This is the team `Quadeyes` submission for `Amazon HackOn 2023`.

## Overview of the Proposed Solution

## Demonstrations

We have designed two client-side applications to show how the developed solution is independent of the client. Both use the same backend model, `Holo`, which we have trained for the user `Eshaan` based on his searching, movie streaming, and music history. You can see the sample interaction here.

### App

https://github.com/EshaanAgg/hackon/assets/96648934/5f9bfd93-1908-46df-80e6-7dd43f961c8f

### Website

https://github.com/EshaanAgg/hackon/assets/96648934/3d94e1f3-3561-4785-8750-245a63549c47

### How does the demo work?

We are using a thin wrapper on `OpenAI` over the `Holo` model, as the same can only give textual responses or choices. We use `OpenAI` as the NLP processor, which decides which kind of recommendation should be provided to the user. We call the right API of the `Holo` model using `OpenAI functions`. Detailed documentation of the internal models used in `Holo` is included below.

Both the clients call the uniformly developed central backend API, which first communicates with OpenAI functions to figure out the right action/model to call in response to the message, calls the same and then calls OpenAI again to present the user in natural text form to the user. Thus, we can build a client-agnostic solution that works on multiple categories of data and is human-interactable.

## Technologies Used

#### 1. Backend Model - Holo:
   - Holo provides personalized recommendations for user Eshaan based on search, movie streaming, and music history.
   - Utilizes historical data to generate tailored textual responses and choices.

#### 2. NLP Processor - OpenAI:
   - OpenAI enhances decision-making by analyzing user queries and determining recommendation types.
   - Acts as a thin wrapper over Holo, integrating seamlessly for a responsive user experience.

#### 3. Web UI - Python with Chainlit:
   - Python with Chainlit framework powers the web UI for interactive user interfaces.
   - Enables easy integration with backend services for fetching and displaying recommendations.

#### 4. Mobile App - Flutter:
   - Flutter framework for cross-platform Android and iOS app development.
   - Leverages Flutter's widget set for a consistent UI, integrates with OpenAI for NLP processing.


