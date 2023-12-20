// Import necessary modules from 'face-api.js'
// import * as faceapi from "face-api.js";
// import * as faceapi from "/node_modules/face-api.js/build/commonjs/index";
// import * as faceapi from "../../node_modules/face-api.js/build/es6/";

async function startVideo() {
  // Load the face-api.js models
  // await faceapi.nets.tinyFaceDetector.loadFromUri("models");
  // await faceapi.nets.faceLandmark68Net.loadFromUri("models");
  // await faceapi.nets.faceRecognitionNet.loadFromUri("models");

  const videoElement = document.getElementById("video");
  const canvasElement = document.getElementById("canvas");
  const displaySize = {
    width: videoElement.width,
    height: videoElement.height,
  };

  console.log(displaySize);
  // faceapi.matchDimensions(canvasElement, displaySize);

  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then((stream) => {
      videoElement.srcObject = stream;
    })
    .catch((error) => {
      console.error("Error accessing webcam:", error);
    });

  videoElement.addEventListener("play", () => {
    const canvasContext = canvasElement.getContext("2d");
    // setInterval(async () => {
    //   const detections = await faceapi
    //     .detectAllFaces(videoElement, new faceapi.TinyFaceDetectorOptions())
    //     .withFaceLandmarks()
    //     .withFaceDescriptors();
    //   const resizedDetections = faceapi.resizeResults(detections, displaySize);
    //   canvasContext.clearRect(0, 0, canvasElement.width, canvasElement.height);
    //   faceapi.draw.drawDetections(canvasElement, resizedDetections);
    //   faceapi.draw.drawFaceLandmarks(canvasElement, resizedDetections);
    // }, 100);
  });
}

// Ensure the 'startVideo' function is called when the DOM is ready
document.addEventListener("DOMContentLoaded", startVideo);
