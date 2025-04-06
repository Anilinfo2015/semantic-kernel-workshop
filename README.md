# Semantic Kernel process flow

```mermaid
flowchart LR  
    Start(Start)--> DoSomeWork(DoSomeWork)
    DoSomeWork--> DoMoreWork(DoMoreWork)
    DoMoreWork--> End(End)
```


```mermaid
flowchart LR  
    Intro(Intro)--> UserInput(User Input)
    UserInput-->|User message == 'exit'| Exit(Exit)
    UserInput-->|User message| AssistantResponse(Assistant Response)
    AssistantResponse--> UserInput
```

## Potato Fries Preparation Process

``` mermaid
flowchart LR
    PreparePotatoFriesEvent([Prepare Potato <br/> Fries Event])
    PotatoFriesReadyEvent([Potato Fries <br/> Ready Event])

    GatherIngredientsStep[Gather Ingredients <br/> Step]
    CutStep[Cut Food <br/> Step]
    FryStep[Fry Food <br/> Step]

    PreparePotatoFriesEvent --> GatherIngredientsStep -->| Slice Potatoes <br/> _Ingredients Gathered_ | CutStep --> |**Potato Sliced Ready** <br/> _Food Sliced Ready_ | FryStep --> |_Fried Food Ready_|PotatoFriesReadyEvent
    FryStep -->|Fried Potato Ruined <br/> _Fried Food Ruined_| GatherIngredientsStep
```

## Seller Process Flow

```mermaid
flowchart LR
    Start(Start) --> EnterProductName(Enter Product Name)
    EnterProductName --> EnterProductDescription(Enter Product Description)
    EnterProductDescription --> ReGenerateDescription(Re-generate Description)
    ReGenerateDescription --> ReviewDescription{Is Description OK?}
    ReviewDescription -- Yes --> GenerateMetadata(Generate Metadata)
    ReviewDescription -- No --> EnterProductDescription
    GenerateMetadata --> ReviewMetadata{Is Metadata OK?}
    ReviewMetadata -- Yes --> UploadImages(Upload Images)
    ReviewMetadata -- No --> GenerateMetadata
    UploadImages --> ReviewImages{Are Images OK?}
    ReviewImages -- Yes --> Submit(Submit)
    ReviewImages -- No --> UploadImages 
```

More Info

https://learn.microsoft.com/en-us/semantic-kernel/frameworks/process/process-framework
https://github.com/microsoft/semantic-kernel/tree/main/dotnet/samples/GettingStartedWithProcesses
