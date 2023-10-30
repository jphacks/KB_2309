import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';
import Capture from "./pages/Capture";
import Header from "./features/header";
import { ChakraProvider } from '@chakra-ui/react'

function App() {
  return (
      <ChakraProvider>
        <div className="App">
        <Header />
        <BrowserRouter>
          <Routes>
            {/* <Route path='/' element={< />}/> */}
            <Route path='/' element={<Capture />}/>
          </Routes>
        </BrowserRouter>
        </div>
      </ChakraProvider>
  );
}

export default App;
