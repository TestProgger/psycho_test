import { Route, Routes } from 'react-router-dom';
import './App.scss';
// import { Container } from '@components/Container'
import { MainPage } from '@pages/Main';



function App() {

  return (
    <Routes>
      <Route path='/' element={<MainPage/>} />
    </Routes>
  )
}

export default App
