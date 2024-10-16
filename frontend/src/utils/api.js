import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';  // Flask server URL

export const fetchProjects = async () => {
    try {
        const response = await axios.get(`${API_URL}/api/projects`);
        return response.data;
    } catch (error) {
        console.error("Error fetching projects:", error);
        return null;
    }
};

export const createProject = async (project) => {
    try {
        const response = await axios.post(`${API_URL}/api/projects`, project);
        return response.data;
    } catch (error) {
        console.error("Error creating project:", error);
        return null;
    }
};