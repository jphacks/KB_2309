import Camera from "../../features/camera";
import Timer from "../../features/timer";
import Percentage from "../../features/percentage";
import Comment from "../../features/comment";
import { Button } from "@chakra-ui/button";
import { Text, Image, Grid, GridItem, Center } from '@chakra-ui/react'
import { ArrowRightIcon } from "@chakra-ui/icons";
import { useState } from "react";
import axios from "axios";

const recordingTime = 24 * 60 * 60 * 1000;
// const recordingTime = 15 * 1000; // for demo
const sampleFeedback = `Remember, improving your posture takes time and practice, but the benefits are worth it! Good posture can help prevent back pain, increase energy levels, and improve overall health.`

function Capture() {
    const [isRecording, setIsRecording] = useState(false);
    const [isSummary, setIsSummary] = useState(false);

    async function onClickStartRecording() {
        console.log("Start Recording");
        setIsRecording(true);
        await axios.get("http://localhost:8080/api/get_ready")
        .then(res => {
            console.log(res.data);
        })
        .catch(err => {
            console.log(err);
        });
        setTimeout(async () => {
            console.log("finish");
            await axios.get("http://localhost:8080/api/summary")
            .then(res => {
                console.log(res.data);
                setIsRecording(false);
                setIsSummary(true);
            })
            .catch(err => {
                console.log(err);
            });
            setIsRecording(false);
            setIsSummary(true);
        }, recordingTime);
    };

    function onClickStopRecording() {
        console.log("Stop Recording");
        setIsRecording(false);
    }

    if (isRecording) {
        return (
            <div style={{marginTop: 100}}>
                <Camera />
                <Button onClick={onClickStopRecording} leftIcon={<ArrowRightIcon />} margin={30} colorScheme="teal" variant="solid" width="400px" height="100px">
                    <Text fontSize="2xl">Stop Recording</Text>
                </Button>
                <Timer expiryTimestamp={Date.now() + recordingTime} />
            </div>
        );
    } else if (isSummary && !isRecording) {
        console.log("Summary");
        return (
            <>
            <Grid
                h='100vh'
                templateRows='repeat(3, 1fr)'
                templateColumns='repeat(4, 1fr)'
                gap={4}
                marginTop={50}
            >
                <GridItem rowSpan={3} colSpan={1} >
                    <Percentage title="Back Angle" percentage={73} result="Good!" color="red" />
                </GridItem>
                <GridItem rowSpan={3} colSpan={1} >
                    <Percentage title="Leg Angle" percentage={49} result="Bad..." color="blue" />
                </GridItem>
                <GridItem rowSpan={2} colSpan={2} >
                    <Image src='../public/frame_3.jpg' alt='Dan Abramov' style={{width:"100%", height:"80vh"}}/>
                </GridItem>
                <GridItem rowSpan={1} colSpan={2} >
                    <Comment text={sampleFeedback}/>
                </GridItem>
            </Grid>
            {/* <Button onClick={() => {setIsSummary(false)}} leftIcon={<ArrowRightIcon />} colorScheme="teal" variant="solid" width="400px" height="100px">
                <Text fontSize="2xl">Back to Home</Text>
            </Button> */}
            </>
        )
    } else if (!isRecording && !isSummary) {
        return (
            <>
            <Center marginTop={"25%"}>
                <Button onClick={onClickStartRecording} leftIcon={<ArrowRightIcon />} colorScheme="teal" variant="solid" width="400px" height="100px">
                    <Text fontSize="2xl">Start Recording</Text>
                </Button>
            </Center>
            </>
        )
    }
    return (
        <>
        </>
    );
}

export default Capture;
