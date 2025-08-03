# Application Architecture Diagram

This Mermaid diagram explains the structure and data flow of the Streamlit data analysis application.

```mermaid
graph TD
    %% Main Application
    A[app.py<br/>Main Streamlit App] --> B[Session State Management]
    A --> C[Sidebar Navigation]
    
    %% Navigation Pages
    C --> D[📁 Subir datos]
    C --> E[📈 Dashboard] 
    C --> F[🤖 Interpretación IA]
    
    %% Upload View Flow
    D --> G[upload_view.py]
    G --> H[File Upload<br/>CSV/XLSX]
    H --> I[data/uploaded_data.csv<br/>Data Persistence]
    I --> J[analyzer.py<br/>analizar_dataframe]
    
    %% Analysis Engine
    J --> K[src/utils.py]
    K --> L[detectar_tipos<br/>Numeric/Categorical/Temporal]
    K --> M[detectar_outliers<br/>IQR Method]
    K --> N[detectar_relaciones<br/>Correlation > 0.75]
    
    %% Machine Learning
    J --> O[sklearn Components]
    O --> P[StandardScaler<br/>Data Normalization]
    O --> Q[KMeans Clustering<br/>Max 3 clusters]
    
    %% AI Integration
    J --> R[AI/AI.py]
    R --> S[LM Studio API<br/>localhost:1234]
    S --> T[meta-llama-3-8b-instruct<br/>Natural Language Interpretation]
    
    %% Results Flow
    J --> U[Analysis Results Dictionary]
    U --> V[Session State Storage]
    
    %% Dashboard View
    E --> W[dashboard_view.py<br/>Basic Display]
    
    %% Interpretation View
    F --> X[interpretation_view.py]
    X --> Y[src/visualizer.py]
    Y --> Z[matplotlib/seaborn<br/>Visualizations]
    Z --> AA[Correlation Heatmaps]
    Z --> BB[Boxplots for Outliers]
    Z --> CC[Scatter Plots]
    
    X --> DD[AI Interpretation Display]
    V --> X
    
    %% Data Dependencies
    subgraph "External Dependencies"
        EE[streamlit]
        FF[pandas]
        GG[scikit-learn]
        HH[matplotlib/seaborn]
        II[requests]
        JJ[numpy]
    end
    
    %% Styling
    classDef mainApp fill:#e1f5fe
    classDef views fill:#f3e5f5
    classDef analysis fill:#e8f5e8
    classDef ai fill:#fff3e0
    classDef data fill:#fce4ec
    
    class A,B,C mainApp
    class D,E,F,G,W,X views
    class J,K,L,M,N,O,P,Q,Y,Z,AA,BB,CC analysis
    class R,S,T,DD ai
    class H,I,U,V data
```

## Architecture Overview

**Application Flow:**
- Main navigation through 3 pages via sidebar
- Data upload → persistence → analysis → visualization → AI interpretation

**Key Components:**
- **Blue**: Main application and navigation
- **Purple**: View components (upload, dashboard, interpretation)
- **Green**: Analysis and visualization modules
- **Orange**: AI integration with LM Studio
- **Pink**: Data storage and session management

**Data Pipeline:**
1. CSV upload through `upload_view.py`
2. Data analysis via `analyzer.py` using utilities
3. Machine learning processing (clustering, scaling)
4. AI interpretation via local LLM
5. Results visualization and display

The diagram shows how the modular architecture separates concerns while maintaining a clear data flow from upload to final AI-powered insights.