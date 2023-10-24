# Amazon HackOn

This is the submission of team `Quadeyes` for `Amazon HackOn 2023`.

## Overview of the Proposed Solution

## Demonstrations

To show how the developed solution is independent of the the client, we have designed two client side applications. Both of them use the same backend model `Holo`, which we have trained for the user `Eshaan` on the basis of his searching, movie streaming and music history. You can see the sample interaction here.

#### App

#### Website

We are using a thin-wrapper on `OpenAI` over the `Holo` model, as the same is only capable of giving textual responses or choices. We use `OpenAI` as the NLP processor, which decides which kind of recommedation should be provided to the user, and calls the right API of the `Holo` model using `OpenAI functions`. Detailed documentation of the internal models used in `Holo` is included below.

## Technologies Used

## Holo: ML Documentation
