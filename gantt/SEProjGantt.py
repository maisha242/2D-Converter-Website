import plotly.express as px
import pandas as pd
from datetime import datetime

# Create the DataFrame
df = pd.DataFrame([
    dict(Task="Ai Study | Scrum92/93/94", Start='2024-12-22', Finish='2025-1-13', Category="ML Development"),
    dict(Task="View Put Request", Start='2024-12-22', Finish='2025-1-3', Category="Frontend"),
    dict(Task="Form Post", Start='2024-12-22', Finish='2025-1-3', Category="Frontend"),
    dict(Task="SageMaker Resource", Start='2024-12-22', Finish='2025-1-13', Category="Cloud"),
    dict(Task="SageMaker Endpoint", Start='2024-12-22', Finish='2025-1-13', Category="Cloud"),
    dict(Task="Website Documentation", Start='2024-12-22', Finish='2025-1-3', Category="Documentation"),
    dict(Task="REPO CLEANUP", Start='2025-3-9', Finish='2025-3-16', Category="Documentation"),
    dict(Task="Syntehtic Orthogonal Multiview render", Start='2025-1-13', Finish='2025-1-26', Category="ML Development"),
    dict(Task="Sketch A Shape: Train/Test eval graph", Start='2025-1-13', Finish='2025-1-26', Category="ML Development"),
    #dict(Task="Setup amplify hosting full stack serverless web", Start='2025-3-27', Finish='2025-4-10', Category="Cloud"),
    #dict(Task="AI integration into AWS", Start='2025-3-27', Finish='2025-4-10', Category="Cloud"),
    dict(Task="Spring Break", Start='2025-3-9', Finish='2025-3-16', Category="Break"),
    dict(Task="Fix API Calls", Start='2025-1-31', Finish='2025-2-7', Category="Frontend"),
    dict(Task="Call SageMaker Endpoint from Frontend", Start='2025-1-31', Finish='2025-2-14', Category="Frontend"),
    dict(Task="Complete ML Data Sketches", Start='2025-1-31', Finish='2025-2-14', Category="ML Development"),
    dict(Task="Stage 2 Components", Start='2025-1-31', Finish='2025-2-14', Category="Frontend"),
    dict(Task="Tracker for Frontend Steps", Start='2025-1-31', Finish='2025-2-14', Category="Frontend"),
    dict(Task="SageMaker Output", Start='2025-1-31', Finish='2025-2-28', Category="Cloud"),
    dict(Task="Dataloader", Start='2025-1-31', Finish='2025-2-21', Category="ML Development"),
    dict(Task="Training Loop", Start='2025-1-31', Finish='2025-2-21', Category="ML Development"),
    dict(Task="Swap Sample Model", Start='2025-2-28', Finish='2025-3-3', Category="ML Development"),
    dict(Task="Testing Framework", Start='2025-3-4', Finish='2025-3-16', Category="ML Development"),
    dict(Task="DSR3", Start='2025-2-28', Finish='2025-3-8', Category="Documentation"),
    # New final project tasks
    dict(Task="Bug Fixes and Documentation", Start='2025-3-16', Finish='2025-4-3', Category="Documentation"),
    dict(Task="Project Poster", Start='2025-4-5', Finish='2025-4-11', Category="Documentation"),
    dict(Task="Final Video", Start='2025-4-5', Finish='2025-4-12', Category="Documentation"),
    dict(Task="Final Technical Document", Start='2025-4-5', Finish='2025-5-1', Category="Documentation"),
    dict(Task="Final Presentation", Start='2025-4-16', Finish='2025-5-3', Category="Documentation"),
    dict(Task="Docusaurus", Start='2025-4-5', Finish='2025-5-1', Category="Documentation"),
    dict(Task="Finalized Project Review", Start='2025-4-28', Finish='2025-5-5', Category="Documentation"),
    dict(Task="Retrospective Meeting Notes", Start='2025-4-28', Finish='2025-5-5', Category="Documentation"),
])

# Convert Start and Finish columns to datetime
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

# Create the timeline plot
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", 
                 color="Category",
                 title="Senior Project Gantt Chart",
                 color_discrete_map={
                     "Documentation": "brown",
                     "ML Development": "green",
                     "Frontend": "darkblue",
                     "Cloud": "royalblue",
                     "Break": "red"
                 })
fig.update_yaxes(autorange="reversed")

# Add vertical lines using add_shape
deadlines = {
    "2025-02-28": "Scope Freeze",
    "2025-04-04": "Code Freeze"
}

for date_str, label in deadlines.items():
    date = datetime.strptime(date_str, "%Y-%m-%d")
    fig.add_shape(
        type="line",
        x0=date, x1=date,
        y0=0, y1=1,
        yref="paper",  # Use paper coordinates for y-axis (0 to 1)
        line=dict(color="red", width=5)
    )
    # Add annotation for the deadline
    fig.add_annotation(
        x=date, y=1.05,  # Position the annotation slightly above the top of the chart
        yref="paper",
        text=label,
        showarrow=False,
        font=dict(color="red", size=12)
    )

se_dept_reviews = {
    "2025-02-20": "Project Review 1",
    "2025-04-15": "Project Review 2",
    "2025-04-26": "PR w/ Sponsors"
}
for date_str, label in se_dept_reviews.items():
    date = datetime.strptime(date_str, "%Y-%m-%d")
    fig.add_shape(
        type="line",
        x0=date, x1=date,
        y0=0, y1=1,
        yref="paper",  # Use paper coordinates for y-axis (0 to 1)
        line=dict(color="green", width=5)
    )
    # Add annotation for the deadline
    fig.add_annotation(
        x=date, y=1.1,  # Increased y position to avoid overlap with other annotations
        yref="paper",
        text=label,
        showarrow=False,
        font=dict(color="green", size=12)
    )

sprints = {
    "2025-01-31": "Sprint 6",
    "2025-02-14": "Sprint 7", 
    "2025-02-28": "Sprint 8",
    "2025-03-14": "Sprint 9",
    "2025-03-28": "Sprint 10",
    "2025-04-11": "Sprint 11",
    "2025-04-25": "Sprint 12"
}
for date_str, label in sprints.items():
    date = datetime.strptime(date_str, "%Y-%m-%d")
    fig.add_shape(
        type="line",
        x0=date, x1=date,
        y0=0, y1=1,
        yref="paper",  # Use paper coordinates for y-axis (0 to 1)
        line=dict(color="blue", width=2, dash="dash")
    )
    # Add annotation for the deadline
    fig.add_annotation(
        x=date, y=1.08,  # Position for sprint annotations
        yref="paper",
        text=label,
        showarrow=False,
        font=dict(color="blue", size=12)
    )
fig.add_vrect(
    x0="2025-02-21", x1="2025-02-28",
    fillcolor="lightcoral", opacity=0.2,  # Light blue with low opacity
    layer="below", line_width=0,
    annotation_text="Scope Freeze Testing", annotation_position="top left",
    annotation_font=dict(color="gray", size=10)
)

fig.add_vrect(
    x0="2025-03-16", x1="2025-04-04",
    fillcolor="lightcoral", opacity=0.2,  # Light coral with low opacity
    layer="below", line_width=0,
    annotation_text="Code Freeze Testing", annotation_position="top left",
    annotation_font=dict(color="gray", size=10)
)
# Show the plot
fig.show()