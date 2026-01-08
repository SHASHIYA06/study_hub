import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import GradeSelection from './pages/GradeSelection';
import Dashboard from './pages/Dashboard';
import SubjectView from './pages/SubjectView';
import ChapterView from './pages/ChapterView';
import AIFeatures from './pages/AIFeatures';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <div className="container">
            <div className="nav-content">
              <Link to="/" className="logo">
                📚 StudyHub
              </Link>
              <div className="nav-links">
                <Link to="/">Home</Link>
                <Link to="/dashboard">Dashboard</Link>
                <Link to="/ai-features">AI Tools</Link>
              </div>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<GradeSelection />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/subject/:subjectId" element={<SubjectView />} />
          <Route path="/chapter/:chapterId" element={<ChapterView />} />
          <Route path="/ai-features" element={<AIFeatures />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
