import { useTimer } from "react-timer-hook";

function Timer({ expiryTimestamp }: { expiryTimestamp: number }) {
const {
    seconds,
    minutes,
    hours,
    days,
    isRunning,
    start,
    pause,
    resume,
    restart,
} = useTimer({
    expiryTimestamp: new Date(expiryTimestamp), // Convert number to Date object

    onExpire: () => console.warn("onExpire called"),
});

return (
    <div style={{ textAlign: "center" }}>
        <h1>the waiting time to make a summary</h1>
        <div style={{ fontSize: "80px" }}>
            <span>{hours}</span>:<span>{minutes}</span>:<span>{seconds}</span>
        </div>
    </div>
);}

export default Timer;
