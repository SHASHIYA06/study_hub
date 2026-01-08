import React, { useState } from 'react';
import { solveDoubt, explainConcept } from '../api';
import { FaRobot, FaQuestionCircle, FaLightbulb } from 'react-icons/fa';
import './AIFeatures.css';

const AIFeatures = () => {
  const [doubt, setDoubt] = useState('');
  const [concept, setConcept] = useState('');
  const [grade, setGrade] = useState('');
  const [doubtSolution, setDoubtSolution] = useState(null);
  const [conceptExplanation, setConceptExplanation] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSolveDoubt = async () => {
    if (!doubt.trim()) {
      alert('Please enter your doubt');
      return;
    }
    
    setLoading(true);
    try {
      const response = await solveDoubt(doubt);
      setDoubtSolution(response.data.solution);
    } catch (err) {
      console.error('Error solving doubt:', err);
      alert('Failed to solve doubt. Please try again.');
    }
    setLoading(false);
  };

  const handleExplainConcept = async () => {
    if (!concept.trim() || !grade.trim()) {
      alert('Please enter both concept and grade');
      return;
    }
    
    setLoading(true);
    try {
      const response = await explainConcept(concept, grade);
      setConceptExplanation(response.data.explanation);
    } catch (err) {
      console.error('Error explaining concept:', err);
      alert('Failed to explain concept. Please try again.');
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <div className="page-header">
        <h1>🤖 AI Learning Tools</h1>
        <p>Get instant help with doubts and concept explanations</p>
      </div>

      <div className="ai-features-grid">
        {/* Doubt Solver */}
        <div className="ai-feature-card">
          <div className="feature-header">
            <FaQuestionCircle className="feature-icon doubt" />
            <h2>Doubt Solver</h2>
          </div>

          <p className="feature-description">
            Ask any question or describe your doubt, and our AI will provide a detailed step-by-step solution.
          </p>

          <textarea
            value={doubt}
            onChange={(e) => setDoubt(e.target.value)}
            placeholder="Enter your doubt or problem here..."
            className="input-textarea"
            rows="5"
          />

          <button
            onClick={handleSolveDoubt}
            disabled={loading}
            className="btn btn-primary"
          >
            {loading ? 'Solving...' : 'Solve Doubt'}
          </button>

          {doubtSolution && (
            <div className="result-box doubt-result">
              <h3>Solution:</h3>
              <div className="result-content">
                {doubtSolution.split('\n').map((line, idx) => (
                  line && <p key={idx}>{line}</p>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Concept Explainer */}
        <div className="ai-feature-card">
          <div className="feature-header">
            <FaLightbulb className="feature-icon concept" />
            <h2>Concept Explainer</h2>
          </div>

          <p className="feature-description">
            Get a detailed explanation of any concept in simple, easy-to-understand language.
          </p>

          <input
            type="text"
            value={concept}
            onChange={(e) => setConcept(e.target.value)}
            placeholder="Enter concept name (e.g., Photosynthesis)"
            className="input-field"
          />

          <input
            type="text"
            value={grade}
            onChange={(e) => setGrade(e.target.value)}
            placeholder="Your grade (e.g., 9, 10)"
            className="input-field"
          />

          <button
            onClick={handleExplainConcept}
            disabled={loading}
            className="btn btn-primary"
          >
            {loading ? 'Explaining...' : 'Get Explanation'}
          </button>

          {conceptExplanation && (
            <div className="result-box concept-result">
              <h3>Explanation:</h3>
              <div className="result-content">
                {conceptExplanation.split('\n').map((line, idx) => (
                  line && <p key={idx}>{line}</p>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default AIFeatures;
