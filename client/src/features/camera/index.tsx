import { useRef, useEffect, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";

const url = 'http://localhost:8080/api/pose_estimate';
const intervalTime = 500;
const bufLimit = 10;
function Camera() {
const webcamRef = useRef<Webcam>(null);
const [bufCount, setBufCount] = useState(0);
const imageBuf = useRef<string[]>([]);
const imageType = 'image/jpeg';
const videoConstraints = {
    width: 720,
    height: 360,
    facingMode: "environment",
};

function getUniqueStr(myStrong: number): string {
    let strong = 1000;
    if (myStrong) strong = myStrong;
    return new Date().getTime().toString(16) + Math.floor(strong*Math.random()).toString(16)
}

useEffect(() => {
    function MultiImagesForm(base64Imgs: string[]): FormData {
        const form = new FormData();
        let cnt = 0;
        for (const base64Img of base64Imgs) {
            const name = getUniqueStr(cnt)+'.jpeg'
            form.append('image_'+cnt, new File([base64Img], name, { type: imageType }));
            cnt++;
        }
        return form;
    }
    const intervalId = setInterval(async () => {
        const imageSrc = webcamRef.current?.getScreenshot();
        if (imageSrc) {
            // Buffering
            if (bufCount >= bufLimit) {
                await axios.post(url, MultiImagesForm(imageBuf.current))
                .then(res => {
                    console.log(`Success` + res.data);
                    imageBuf.current = [];
                    setBufCount(0);
                })
                .catch(err => {
                    console.log(err);
                });
            } else {
                imageBuf.current.push(imageSrc);
                setBufCount(bufCount + 1);
            }
        }
    }, intervalTime);
    return () => {
        clearInterval(intervalId);
    };
}, [imageBuf, bufCount]);

return (
    <Webcam
        audio={false}
        width={540}
        height={360}
        ref={webcamRef}
        screenshotFormat={imageType}
        videoConstraints={videoConstraints}
    />
);
}

export default Camera;
