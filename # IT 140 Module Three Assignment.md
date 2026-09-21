# IT 140 Module Three Assignment
# Paycheck Calculator Pseudocode Template
#
# Complete the TODO prompts below with your own pseudocode.
# Keep this file in .pseudo format for submission.
#
# Your finished pseudocode should represent the same logic as your flowchart.
# Use clear indentation and appropriate pseudocode keywords such as
# INPUT, LET, IF, ELSE, and OUTPUT where they fit your design.

BEGIN
    // Payment rates
    REG_RATE = 20
    OT_RATE = 30
    
    //Input
    Display "Enter hours worked: "
    Input hours_worked

    // Decision branching & Processes
    IF hours_worked <= 40 THEN
        tot_pay = hours_worked * REG_RATE
    ELSE
        ot_hours = hours_worked - 40
        reg_pay = 40 * REG_RATE
        ot_pay = ot_hours * OT_RATE
        tot_pay = reg_pay + OT_RATE
    END IF

    // Output
    Display "Your total paycheck is: $", tot_pay 
END