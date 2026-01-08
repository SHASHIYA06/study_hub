import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchGrades } from '../api';
import './GradeSelection.css';

const GradeSelection = () => {
  const [grades, setGrades] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadGrades = async () => {
      try {
        const response = await fetchGrades();
        setGrades(response.data.results || response.data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching grades:', err);
        setError('Failed to load grades. Please try again.');
        setLoading(false);
      }
    };
    loadGrades();
  }, []);

  const getGradeEmoji = (level) => {
    const emojis = {
      'nursery': '👶',
      'ukg': '🧒',
      'kg': '👧',
    };
    
    for (let i = 1; i <= 12; i++) {
      if (level === `class_${i}`) {
        return i <= 5 ? '📚' : i <= 10 ? '🎓' : '🏆';
      }
    }
    return emojis[level] || '📖';
  };

  if (loading) {
    return <div className="loading">Loading grades...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="container">
      <div className="page-header">
        <h1>Choose Your Grade</h1>
        <p>Select your current grade to start learning</p>
      </div>

      <div className="grade-grid">
        {grades.map((grade) => (
          <Link 
            key={grade.id} 
            to={`/dashboard?grade=${grade.id}`}
            className="grade-card"
          >
            <div className="grade-emoji">{getGradeEmoji(grade.level)}</div>
            <h3>{grade.level.replace('_', ' ').toUpperCase()}</h3>
            <p>{grade.description}</p>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default GradeSelection;
