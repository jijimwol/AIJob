
var field = document.getElementById("field");
var discription=document.getElementById("discription");
var resume_area=document.getElementById("resume_area");
var button=document.getElementById("button");
var main_area=document.getElementById("main_area");
var hr=document.getElementById("hr");
function start() {
    field.style.display = "none";
    resume_area.style.display = "none";
    discription.style.display = "none";
    button.style.display = "none";
    hr.style.display = "none";
    main_area.style.display = "flex";
}
var feedbacke=document.getElementById("feedback-card");
var answere=document.getElementById("answer-card");
function feedback()
{
    if(feedbacke.style.display == "flex")
    {
        feedbacke.style.display = "none";
    }
    else{
        feedbacke.style.display = "flex";
    }
}
function answer()
{
    if(answere.style.display == "flex")
        {
            answere.style.display = "none";
        }
        else{
            answere.style.display = "flex";
        }
}
var aud = document.getElementById("audio-upload");
var tex = document.getElementById("textarea");

function showAudio() {
    aud.style.display = "block";
    tex.style.display = "none";
}

function showTextarea() 
{
    aud.style.display = "none";
    tex.style.display = "block";
}
function feedback_ans()
{
    feedbacke.style.display = "flex";
    answere.style.display = "flex";
}