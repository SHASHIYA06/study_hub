import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { fetchChapters } from '../api';
import './SubjectView.css';

const SubjectView = () => {
  const { subjectId } = useParams();
  const [chapters, setChapters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadChapters = async () => {
      try {
        const response = await fetchChapters(subjectId);
        setChapters(response.data.results || response.data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching chapters:', err);
        setError('Failed to load chapters. Please try again.');
        setLoading(false);
      }
    };
    loadChapters();
  }, [subjectId]);

  if (loading) {
    return <div className="loading">Loading chapters...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="container">
      <div className="page-header">
        <h1>📖 Chapters</h1>
        <p>Select a chapter to explore study materials</p>
      </div>

      <div className="chapters-grid">
        {chapters.map((chapter) => (
          <Link 
            key={chapter.id} 
            to={`/chapter/${chapter.id}`}
            className="chapter-card"
          >
            <div className="chapter-header">
              <div className="chapter-number">
                Chapter {chapter.chapter_number}
              </div>
              <div className="materials-badge">
                {chapter.materials?.length || 0} Materials
              </div>
            </div>
            
            <h3>{chapter.title}</h3>
            <p>{chapter.description}</p>

            {chapter.materials && chapter.materials.length > 0 && (
              <div className="material-types">
                {chapter.materials.slice(0, 3).map((material) => (
                  <span key={material.id} className="material-tag">
                    {material.material_type}
                  </span>
                ))}
              </div>
            )}
          </Link>
        ))}
      </div>
    </div>
  );
};

export default SubjectView;
