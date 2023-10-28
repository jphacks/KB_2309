import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';
import Capture from "./pages/Capture";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
          <Routes>
            {/* <Route path='/' element={< />}/> */}
            <Route path='/capture' element={<Capture />}/>
          </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
