import React, { useState, useEffect } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { fetchSubjects } from '../api';
import { FaBook, FaVideo, FaClipboardList } from 'react-icons/fa';
import './Dashboard.css';

const Dashboard = () => {
  const [searchParams] = useSearchParams();
  const [subjects, setSubjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const gradeId = searchParams.get('grade');

  useEffect(() => {
    const loadSubjects = async () => {
      try {
        const response = await fetchSubjects(gradeId);
        setSubjects(response.data.results || response.data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching subjects:', err);
        setError('Failed to load subjects. Please try again.');
        setLoading(false);
      }
    };

    if (gradeId) {
      loadSubjects();
    }
  }, [gradeId]);

  const subjectEmojis = {
    'english': '📖',
    'mathematics': '🔢',
    'science': '🔬',
    'social_studies': '🌍',
    'hindi': '🇮🇳',
    'physics': '⚛️',
    'chemistry': '🧪',
    'biology': '🦠',
    'history': '🏛️',
    'geography': '🗺️',
    'economics': '💰',
  };

  if (loading) {
    return <div className="loading">Loading subjects...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="container">
      <div className="page-header">
        <h1>📚 Subjects</h1>
        <p>Choose a subject to explore chapters and materials</p>
      </div>

      <div className="subjects-grid">
        {subjects.map((subject) => (
          <Link 
            key={subject.id} 
            to={`/subject/${subject.id}`}
            className="subject-card"
          >
            <div className="subject-icon">
              {subjectEmojis[subject.name] || '📚'}
            </div>
            <h3>{subject.name.replace('_', ' ').toUpperCase()}</h3>
            <p>{subject.description}</p>

            <div className="subject-features">
              <div className="feature">
                <FaBook className="feature-icon" />
                <span>Chapters</span>
              </div>
              <div className="feature">
                <FaVideo className="feature-icon video" />
                <span>Videos</span>
              </div>
              <div className="feature">
                <FaClipboardList className="feature-icon quiz" />
                <span>Quizzes</span>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
