import { Navigate, Route, Routes } from 'react-router-dom';
import './App.scss';
// import { Container } from '@components/Container'
import MainPage from '@pages/Main';
import ListTestsPage from '@pages/ListTests';
import Error from '@components/Error';
import { observer } from 'mobx-react-lite';
import { usePersistentStore } from '@store';



function App() {

  const {subject} = usePersistentStore();

  if(subject?.secret){
    console.log(subject.secret)
    return (
      <>
        <Routes>
          <Route path='/tests' element={<ListTestsPage/>} />

          <Route path='*' element={<Navigate to={'/tests'}/>} />
        </Routes>
        <Error/>
      </>
    )
  }
  else{
    return (
      <>
        <Routes>
          <Route path='/' element={<MainPage/>} />
        </Routes>
        <Error/>
      </>
    )
  }
}

export default observer(App)
