window.onload = init;


function init(){
    var videoObj = { "video": true }
    errBack = function(error){alert("Video capture error: ", error.code);};  
    ask(videoObj,errBack);  
    var btn_camera = document.getElementById("btn_photo");
    btn_camera.addEventListener('click',take_photo);
}



function ask(videoObj,errBack){
    if(navigator.getUserMedia){                    // Standard
        navigator.getUserMedia(videoObj, startWebcam, errBack);
    }else if(navigator.webkitGetUserMedia){        // WebKit
        navigator.webkitGetUserMedia(videoObj, startWebcam, errBack);
    }else if(navigator.mozGetUserMedia){     // Firefox
        navigator.mozGetUserMedia(videoObj, startWebcam, errBack);
    };
}

function startWebcam(stream){

    video = document.getElementById('video')
    canvas = document.getElementById('canvas_1')
    video.width = video.offsetWidth;
    if(navigator.getUserMedia){                    // Standard
        video.srcObject = stream;
        video.play();
    }else if(navigator.webkitGetUserMedia){        // WebKit
        video.srcObject = window.webkitURL.createObjectURL(stream);
        video.play();
    }else if(navigator.mozGetUserMedia){        // Firefox
        video.srcObject = stream
        video.play();
    }
}

function take_photo() {
    saver();
}

function saver()
{
    document.getElementById("btn_photo").addEventListener("click", ajax);
}


function ajax()
{
        var video = document.getElementById('video');
        var canvas = document.createElement('CANVAS');
        var ctx = canvas.getContext('2d');
        canvas.height = 448
        canvas.width = 448;
        ctx.drawImage(video, 100, 30, 448, 448, 0, 0, 448, 448);
        var dataUrl = canvas.toDataURL();
        console.log(dataUrl);
        $.ajax({
            type: "POST", 
            url: "camsave.php",
            data: { imgBase64: dataUrl},
            success: function(){
                alert("Analyse terminée");
            },
            error: function(xhr, status, error) {
                alert("echec");
            }
        }).done(function (response, textStatus, jqXHR){
            if(response==0)
                $("#result").html("Il semble que vous êtes une femme");
            else
                $("#result").html("Il semble que vous êtes un homme");
        });
}