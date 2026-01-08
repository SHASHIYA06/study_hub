import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Grades
export const fetchGrades = () => api.get('/grades/');
export const fetchGrade = (id) => api.get(`/grades/${id}/`);

// Subjects
export const fetchSubjects = (gradeId) => {
  const params = gradeId ? { grade_id: gradeId } : {};
  return api.get('/subjects/', { params });
};
export const fetchSubject = (id) => api.get(`/subjects/${id}/`);

// Chapters
export const fetchChapters = (subjectId) => {
  const params = subjectId ? { subject_id: subjectId } : {};
  return api.get('/chapters/', { params });
};
export const fetchChapter = (id) => api.get(`/chapters/${id}/`);
export const fetchVideos = (chapterId) => api.get(`/chapters/${chapterId}/fetch_videos/`);
export const generateSummary = (chapterId) => api.post(`/chapters/${chapterId}/generate_summary/`);
export const generateQuiz = (chapterId, numQuestions = 10) => 
  api.post(`/chapters/${chapterId}/generate_quiz/`, { num_questions: numQuestions });
export const generateFlashcards = (chapterId, numCards = 10) => 
  api.post(`/chapters/${chapterId}/generate_flashcards/`, { num_cards: numCards });

// Study Materials
export const fetchMaterials = (chapterId) => {
  const params = chapterId ? { chapter_id: chapterId } : {};
  return api.get('/materials/', { params });
};

// Quizzes
export const fetchQuizzes = (chapterId) => {
  const params = chapterId ? { chapter_id: chapterId } : {};
  return api.get('/quizzes/', { params });
};

// Flashcards
export const fetchFlashcards = (chapterId) => {
  const params = chapterId ? { chapter_id: chapterId } : {};
  return api.get('/flashcards/', { params });
};

// AI Features
export const solveDoubt = (problemDescription) => 
  api.post('/doubt-solver/ask_doubt/', { problem_description: problemDescription });

export const explainConcept = (concept, grade) => 
  api.post('/explain/explain/', { concept, grade });

export default api;
