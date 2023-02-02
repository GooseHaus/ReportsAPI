import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = 


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        
        studentName = request.form["studentName"]
        studentGrade = request.form["studentMark"]
        courseDesc = request.form["courseDesc"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(studentName, studentGrade, courseDesc),
            temperature=0.8,
            max_tokens=3000,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(studentName, studentGrade, courseDesc):
    if int(studentGrade) >79:

        return ("""Write a three sentance report card comment for the studentName. 
        The first two sentances must each include at least one entry from the list: 
        thorough, high degree, extensive, comprehensive, in-depth, admirable, outstanding, tremendous. 
        The third sentance must be a suggestion for how to improve. Keep it positive. 
        All three sentances should be reasonably related to the courseDesc. 

                studentName: Hayyan
                courseDesc: The Grade 12 Computer Science program challenged students to further develop 
                their knowledge and skills in computer science, focusing largely on the topic of 
                object-oriented design. The class analysed algorithms for runtime efficiency, 
                extended their understanding of arrays to a second dimension, and began to use 
                recursive definitions to break tasks into solvable self-similar base cases, 
                and learned to include abstraction in their class hierarchy definitions. 
                At the end of the year, each member of the class 
                used modular design principles and two-dimensional arrays to create playable games 
                making use of predefined custom classes according to the software development life cycle. 
                Report Card Comment: Hayyan has had an outstanding year in his AP Computer Science class, 
                showing a thorough understanding of the benefits of class hierarchy. 
                His final project where he built a tabletop card game demonstrated extensive ability 
                to iteratively apply the software design lifecycle. 
                Hayyan is encouraged to investigate new programming concepts and languages as he moves 
                into his post-secondary studies. 

                studentName: Siyang
                courseDesc: The Grade 11 Functions program covered concepts that included exponential 
                functions, trigonometry, periodic functions, sequences, series, and financial mathematics. 
                Students explored the characteristics of relationships of exponential growth and geometric series. 
                The class revisited the trigonometric laws and identities and extended their 
                understanding by applying transformations to sinusoidal wave functions. 
                In the Financial Applications unit, 
                students were required to compare results of various investment or debt scenarios using time value 
                of money calculations and communicate their analysis of the results. 
                Report Card Comment: 
                Siyang had a tremendous semester in the grade eleven Functions program, 
                demonstrating admirable ability to manipulate and transform the function families explored throughout. 
                Her final assessment further illustrated a comprehensive understanding of optimization and 
                problem-solving strategies allowing her to slightly improve her overall mark. 
                Siyang is encouraged to continue working collaboratively with her peers when reviewing 
                mathematics concepts to broaden her exposure to problem solving strategies. 

                studentName: {}
                courseDesc: {}
                Report Card Comment:""").format(
                        studentName.capitalize(),
                        courseDesc.capitalize(),
                    )

    elif int(studentGrade) >69:

        return ("""Write a three sentance report card comment for the studentName. 
        The first two sentances must each include at least one entry from the list: 
        considerable, significant, substantial, noteworthy, strong, ample. 
        The third sentance must be a suggestion for how to improve. Keep it positive. 
        All three sentances should be reasonably related to the courseDesc. 

                studentName: Tom
                courseDesc: The Grade 12 Computer Science program challenged students to further develop 
                their knowledge and skills in computer science, focusing largely on the topic of 
                object-oriented design. The class analysed algorithms for runtime efficiency, 
                extended their understanding of arrays to a second dimension, and began to use 
                recursive definitions to break tasks into solvable self-similar base cases, 
                and learned to include abstraction in their class hierarchy definitions. 
                At the end of the year, each member of the class 
                used modular design principles and two-dimensional arrays to create playable games 
                making use of predefined custom classes according to the software development life cycle. 
                Report Card Comment: Tom had a noteworthy year in his AP Computer Science class, 
                showing a considerable understanding of the benefits of class hierarchy. 
                His final project demonstrated significant ability to iteratively apply the software design lifecycle. 
                Tom is encouraged to investigate new programming concepts and languages as he moves 
                into his post-secondary studies. 

                studentName: Ethan
                courseDesc: The Grade 11 Functions program covered concepts that included exponential 
                functions, trigonometry, periodic functions, sequences, series, and financial mathematics. 
                Students explored the characteristics of relationships of exponential growth and geometric series. 
                The class revisited the trigonometric laws and identities and extended their 
                understanding by applying transformations to sinusoidal wave functions. 
                In the Financial Applications unit, 
                students were required to compare results of various investment or debt scenarios using time value 
                of money calculations and communicate their analysis of the results. 
                Report Card Comment: 
                Ethan had a strong semester in the grade eleven Functions program, demonstrating substantial 
                ability to manipulate and transform the function families explored throughout. 
                His final assessment, while still demonstrated ample ability to recall concepts from throughout the semester. 
                I encourage Ethan to become more familiar with the special triangles that he can use 
                to calculate the exact values of trigonometric ratios, rather than relying on his calculator.  

                studentName: {}
                courseDesc: {}
                Report Card Comment:""").format(
                        studentName.capitalize(),
                        courseDesc.capitalize(),
                    )
    
    elif int(studentGrade) >59:

        return ("""Write a three sentance report card comment for the studentName. 
        The first two sentances must each include at least one entry from the list: 
        some, moderate, modest, adequate, satisfactory. 
        The third sentance must be a suggestion for how to improve. 
        All three sentances should be reasonably related to the courseDesc. 

                studentName: Jake
                courseDesc: The Grade 11 Functions program covered concepts that included exponential 
                functions, trigonometry, periodic functions, sequences, series, and financial mathematics. 
                Students explored the characteristics of relationships of exponential growth and geometric series. 
                The class revisited the trigonometric laws and identities and extended their 
                understanding by applying transformations to sinusoidal wave functions. 
                In the Financial Applications unit, 
                students were required to compare results of various investment or debt scenarios using time value 
                of money calculations and communicate their analysis of the results. 
                Report Card Comment: Jake had some success this semester in the grade eleven Functions program, 
                demonstrating moderate ability to improve his understanding throughout. His final assessment 
                demonstrated a more modest ability to recall and revise the content explored throughout the semester. 
                I encourage Jake to become more familiar with the special triangles that he can use to 
                calculate the exact values of trigonometric ratios, rather than relying on his calculator.  

                studentName: Luna
                courseDesc: In the Grade 12 Calculus and Vectors program students developed their understanding 
                of calculus concepts including tangents, limits, and derivatives both from first principles 
                and using the various algebraic rules, such as the chain rule. The class then looked at 
                multiple strategies for solving limits and derivatives and utilized them to develop accurate 
                representations of the graphs of expressions to locate optimal values, asymptotes, ranges 
                of increase and decrease, as well as ranges of concavity. 
                Report Card Comment: Luna had a satifactory end to her semester in the Calculus and Vectors program, 
                demonstrating some ability to make vector calculations. Her final assessment further illustrated a 
                modest recall and development of optimization and problem-solving strategies allowing her to 
                maintain her overall mark. Luna is encouraged to leverage her collaborative work skills to 
                develop her mathematical abilities. 

                studentName: {}
                courseDesc: {}
                Report Card Comment:""").format(
                        studentName.capitalize(),
                        courseDesc.capitalize(),
                    )
    
    elif int(studentGrade) >49:

        return ("""Write a three sentance report card comment for the studentName. 
        The first two sentances must each include at least one entry from the list: 
        limited, minimal, little, slight, insufficient, inadequate. 
        The third sentance must be a suggestion for how to improve. Be positive, but modest.  
        All three sentances should be reasonably related to the courseDesc. 

                studentName: Jack
                courseDesc: The Grade 11 Functions program covered concepts that included exponential 
                functions, trigonometry, periodic functions, sequences, series, and financial mathematics. 
                Students explored the characteristics of relationships of exponential growth and geometric series. 
                The class revisited the trigonometric laws and identities and extended their 
                understanding by applying transformations to sinusoidal wave functions. 
                In the Financial Applications unit, 
                students were required to compare results of various investment or debt scenarios using time value 
                of money calculations and communicate their analysis of the results. 
                Report Card Comment: Jack had limited success this semester in the grade eleven Functions program, 
                demonstrating minimal ability to improve his understanding throughout. His final assessment 
                demonstrated an inadequate ability to recall and revise the content explored throughout the semester. 
                I encourage Jack to regularly complete his assigned homework.   

                studentName: Liana
                courseDesc: In the Grade 12 Calculus and Vectors program students developed their understanding 
                of calculus concepts including tangents, limits, and derivatives both from first principles 
                and using the various algebraic rules, such as the chain rule. The class then looked at 
                multiple strategies for solving limits and derivatives and utilized them to develop accurate 
                representations of the graphs of expressions to locate optimal values, asymptotes, ranges 
                of increase and decrease, as well as ranges of concavity. 
                Report Card Comment: Liana had a tough end to her semester in the Calculus and Vectors program, 
                demonstrating little ability to make vector calculations. Her final assessment further illustrated a 
                limited recall of optimization and problem-solving strategies further dropping her mark. 
                Liana is encouraged to leverage her collaborative work skills to develop her mathematical abilities. 

                studentName: {}
                courseDesc: {}
                Report Card Comment:""").format(
                        studentName.capitalize(),
                        courseDesc.capitalize(),
                    )
    
    else :

        return ("""Write a three sentance report card comment for the studentName.
            Indicate that they did not pass the course. 
            Suggest that they consider retaking the course. 

            studentName: Hank
            Report Card Comment: Hank has shown a lack of mastery in the course material. 
            Although they have put in a great effort, they have not been able to achieve a passing grade. 
            It is recommended that Hank consider retaking the course in the future to strengthen their 
            knowledge and skills in this area.
            
            studentName: {}
            Report Card Comment:""").format(
                        studentName.capitalize()
                    )
