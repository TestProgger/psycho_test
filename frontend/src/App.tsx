import { Navigate, Route, Routes } from 'react-router-dom';
import './App.scss';
import MainPage from '@pages/Main';
import ListTestsPage from '@pages/ListTests';
import Error from '@components/Error';
import { observer } from 'mobx-react-lite';
import { usePersistentStore } from '@store';
import TestPage from '@pages/Test';
import { useEffect } from 'react';



function App() {

  const {subject} = usePersistentStore();

  useEffect(() => {
    if(subject.expires && subject.expires < new Date()){
      subject.clear()
    }
  }, [])

  if(subject?.is_authenticated){
    return (
      <>
        <Routes>
          <Route path='/tests' element={<ListTestsPage/>} />
          <Route path='/test/:id' element={<TestPage/>} />
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
          <Route path='*' element={<Navigate to={'/'}/>} />
        </Routes>
        <Error/>
      </>
    )
  }
}

export default observer(App)
