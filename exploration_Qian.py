import pandas as pd
import plotly.express as px

#1
data = pd.read_csv('./revised_csbs.csv')
fig1 = px.scatter(data, x="currentapprovalamount", y="forgivenessamount", color="community_bank",
                 facet_col="state_chartered", facet_row="income_area_of_business")
fig1.update_layout(title='Scatter Plot for Approval Amount and Forgiveness Amount',
                   xaxis=dict(title='Current Approval Amount($)'),
                   yaxis=dict(title='Forgiveness Amount($)'))
fig1.write_html("general_amount_plot.html")


#2
fig2 = px.histogram(data, x="currentapprovalamount", y="forgivenessamount", color="minority",
                   marginal="box", # or violin, rug
                   hover_data=data.columns)
fig2.update_layout(title='Comparison the Difference between Minority and Non-minority Bank ',
                   xaxis=dict(title='Current Approval Amount($)'),
                   yaxis=dict(title='Sum of Forgiveness Amount($)'))
fig2.write_html("minority_plot.html")


#3
fig3 = px.scatter(data, x="currentapprovalamount", y="forgivenessamount",
                 size="forgivenessamount", color="originatinglenderstate",
                 hover_name="originatinglenderstate", log_x=True, size_max=30)
fig3.update_layout(title='Bubble Chart for Approval Amount and Forgiveness Amount',
                  xaxis=dict(title='Current Approval Amount($)'),
                  yaxis=dict(title='Forgiveness Amount($)'))
fig3.write_html("Bubble Chart.html")

#4
data = data.sort_values(by=['currentapprovalamount'])
fig4 =px.scatter(data, x="currentapprovalamount", y="forgivenessamount", animation_frame="approval_range",
               animation_group="originatinglenderstate",
               size="forgivenessamount", color="originatinglenderstate", hover_name="originatinglenderstate",
               log_x=True, size_max=50, range_y=[0,200000])
fig4.write_html("Bubble_Chart_Animation.html")
