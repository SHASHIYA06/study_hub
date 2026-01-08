import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { fetchChapter, fetchVideos, generateSummary, generateFlashcards } from '../api';
import { FaVideo, FaFileAlt, FaLightbulb } from 'react-icons/fa';
import './ChapterView.css';

const ChapterView = () => {
  const { chapterId } = useParams();
  const [chapter, setChapter] = useState(null);
  const [videos, setVideos] = useState([]);
  const [summary, setSummary] = useState(null);
  const [flashcards, setFlashcards] = useState([]);
  const [loading, setLoading] = useState(true);
  const [videoLoading, setVideoLoading] = useState(false);
  const [summaryLoading, setSummaryLoading] = useState(false);
  const [flashcardsLoading, setFlashcardsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadChapter = async () => {
      try {
        const response = await fetchChapter(chapterId);
        setChapter(response.data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching chapter:', err);
        setError('Failed to load chapter. Please try again.');
        setLoading(false);
      }
    };
    loadChapter();
  }, [chapterId]);

  const handleFetchVideos = async () => {
    setVideoLoading(true);
    try {
      const response = await fetchVideos(chapterId);
      setVideos(response.data.videos);
    } catch (err) {
      console.error('Error fetching videos:', err);
      alert('Failed to fetch videos. Please try again.');
    }
    setVideoLoading(false);
  };

  const handleGenerateSummary = async () => {
    setSummaryLoading(true);
    try {
      const response = await generateSummary(chapterId);
      setSummary(response.data.summary);
    } catch (err) {
      console.error('Error generating summary:', err);
      alert('Failed to generate summary. Make sure the chapter has content.');
    }
    setSummaryLoading(false);
  };

  const handleGenerateFlashcards = async () => {
    setFlashcardsLoading(true);
    try {
      const response = await generateFlashcards(chapterId, 10);
      setFlashcards(response.data);
    } catch (err) {
      console.error('Error generating flashcards:', err);
      alert('Failed to generate flashcards. Make sure the chapter has content.');
    }
    setFlashcardsLoading(false);
  };

  if (loading) {
    return <div className="loading">Loading chapter...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  if (!chapter) {
    return <div className="error">Chapter not found</div>;
  }

  return (
    <div className="container">
      <div className="chapter-header-section">
        <h1>Chapter {chapter.chapter_number}: {chapter.title}</h1>
        <p>{chapter.description}</p>
      </div>

      {/* AI Tools Section */}
      <div className="ai-tools-grid">
        <button 
          onClick={handleFetchVideos}
          className="ai-tool-btn video-btn"
          disabled={videoLoading}
        >
          <FaVideo />
          <span>{videoLoading ? 'Fetching...' : 'Fetch Videos'}</span>
        </button>

        <button 
          onClick={handleGenerateSummary}
          className="ai-tool-btn summary-btn"
          disabled={summaryLoading}
        >
          <FaFileAlt />
          <span>{summaryLoading ? 'Generating...' : 'Generate Summary'}</span>
        </button>

        <button 
          onClick={handleGenerateFlashcards}
          className="ai-tool-btn flashcard-btn"
          disabled={flashcardsLoading}
        >
          <FaLightbulb />
          <span>{flashcardsLoading ? 'Generating...' : 'Generate Flashcards'}</span>
        </button>
      </div>

      {/* Videos Section */}
      {videos.length > 0 && (
        <section className="content-section">
          <h2>📹 Educational Videos</h2>
          <div className="videos-grid">
            {videos.map((video, idx) => (
              <div key={idx} className="video-card">
                <img 
                  src={video.thumbnail} 
                  alt={video.title}
                  className="video-thumbnail"
                />
                <div className="video-info">
                  <h3>{video.title}</h3>
                  <p className="channel-name">{video.channel}</p>
                  <a
                    href={`https://youtube.com/watch?v=${video.video_id}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn btn-primary"
                  >
                    Watch Now
                  </a>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Summary Section */}
      {summary && (
        <section className="content-section summary-section">
          <h2>📝 Chapter Summary</h2>
          <div className="summary-content">
            {summary.split('\n').map((line, idx) => (
              line && <p key={idx}>{line}</p>
            ))}
          </div>
        </section>
      )}

      {/* Flashcards Section */}
      {flashcards.length > 0 && (
        <section className="content-section flashcards-section">
          <h2>🎴 Flashcards</h2>
          <div className="flashcards-grid">
            {flashcards.map((card, idx) => (
              <div key={idx} className="flashcard">
                <div className="flashcard-question">
                  <strong>Q:</strong> {card.question}
                </div>
                <div className="flashcard-answer">
                  <strong>A:</strong> {card.answer}
                </div>
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
};

export default ChapterView;
