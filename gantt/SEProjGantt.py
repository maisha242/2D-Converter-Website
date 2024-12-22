import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Ai Study | Scrum92/93/94", Start='2024-12-22', Finish='2025-1-13'),
    dict(Task="View Put Request", Start='2024-12-22', Finish='2025-1-3'),
    dict(Task="Form Post", Start='2024-12-22', Finish='2025-1-3'),
    dict(Task="SageMaker Resource", Start='2024-12-22', Finish='2025-1-13'),
    dict(Task="SageMaker Endpoint", Start='2024-12-22', Finish='2025-1-13'),
    dict(Task="Website Documentation", Start='2024-12-22', Finish='2025-1-3'),
    dict(Task="Pixel2Mesh: Dev Prep Resrouces", Start='2024-12-22', Finish='2025-1-13'),
    dict(Task="REPO CLEANUP", Start='2024-12-22', Finish='2025-1-3'),
    dict(Task="Pixel2Mesh: Run+Examine PyTorch/TF code", Start='2024-12-22', Finish='2025-1-13'),
    dict(Task="Syntehtic Orthogonal Multiview render", Start='2025-1-13', Finish='2025-1-26'),
    dict(Task="Sketch A Shape: Train/Test eval graph", Start='2025-1-13', Finish='2025-1-26'),
    dict(Task="Setup amplify hosting full stack serverless web", Start='2025-3-27', Finish='2025-4-10'),
    dict(Task="mask git approach (+reading)", Start='2025-1-13', Finish='2025-1-26'),
    dict(Task="Ai integration into  AWS", Start='2025-3-27', Finish='2025-4-10'),

])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", title="Senior Project Gantt Chart")
fig.update_yaxes(autorange="reversed")
fig.show()

#front changes from sponsors = amount unknown

# Epic: Sketch a shape/ Pixel 2 mesh
# syntehtic orthogonal drawing: quantity generation
    #45 degree above view, 15 degrees changes to cover 360
 



