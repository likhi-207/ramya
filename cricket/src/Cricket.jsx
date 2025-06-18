import React, { useState } from 'react' 
import "./Cricket.css"
const CricketScore = (props) => {
    console.log("props" ,props)
    console.log("targert = " , props.target)
    const [runs , setRuns] = useState(0);
    const [wickets , setWickets] = useState(0);
    const [overs,setOvers]=useState(0);
    const [balls,setBalls]=useState(0);
    const [currentOver,setCurrentOver]=useState(0);
    const [remainingOvers,setRemainingOvers]=useState(0);
    const [target , setTarget] = useState(props.target);

    const handleSix=()=>{
        setRuns(runs+6);
    }

    const handleFour=()=>{
        setRuns(runs+4);
    }

    const handleThree=()=>{
        setRuns(runs+3);
    }

    const handleTwo=()=>{
        setRuns(runs+2);
    }

    const handleOne=()=>{
        setRuns(runs+1);
    }

    const handleDot=()=>{
        setRuns(runs+0);
    }

    const updatedOver=()=>{
        if(remainingOvers>0)
            setCurrentOvers(remainingOvers-1);
    }

    const handleRuns=(run)=>{
        if(runs+run>=setTarget)
            alert("Target Chased");
        setRuns(run+run);
    }

    const handleWicket=()=>{
        if(wickets+1==10)
            alert("All out");
        setWickets(wicket+1);

    }

return (
    <>
    <h1>score:{runs}/{wickets}</h1>
    <h3>currentOver:{overs}.{balls}</h3>
    <h3>remainingOvers:{reamainingOvers}</h3>
    {
        wickets<10 && runs+target ?
        <div>
            <button onClick={handleSix}>Six</button>
            <button onClick={handleFour}>Four</button>
            <button onClick={handleThree}>Three</button>
            <button onClick={handleTwo}>Two</button>
            <button onClick={handleOne}>One</button>
            <button onClick={handleDot}>Dot</button>
            <button onClick={handleWicket}>Wickets</button>
            <button onClick={updatedOver}>nextOver</button>

    </div>
    :
        <h3>Game over</h3>
}
    </>
  )
}
 export default Cricket;

