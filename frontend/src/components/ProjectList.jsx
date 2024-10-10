import { useState, useEffect } from 'react';
import { fetchProjects, createProject } from '../utils/api';

const ProjectList = () => {
    const [projects, setProjects] = useState([]);
    const [newProject, setNewProject] = useState({ name: '', short_name: '' });

    useEffect(() => {
        const getProjects = async () => {
            const data = await fetchProjects();
            setProjects(data);
        };

        getProjects();
    }, []);

    const handleInputChange = (e) => {
        setNewProject({
            ...newProject,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const createdProject = await createProject(newProject);
        setProjects([...projects, createdProject]);                 // Add new project to state
        setNewProject({ name: '', short_name: '' });                // Clear form
    };

    return (
        <div>
            <h1>Projects</h1>
            <ul>
                {projects.map(project => (
                    <li key={project._id}>{project.name}</li>
                ))}
            </ul>

            {/* Project creation form */}
            <h2>Create a New Project</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="name"
                    value={newProject.name}
                    onChange={handleInputChange}
                    placeholder="Project Name"
                    required
                />
                <input
                    type="text"
                    name="short_name"
                    value={newProject.short_name}
                    onChange={handleInputChange}
                    placeholder="Short Name"
                    required
                />
                <button type="submit">Create Project</button>
            </form>
        </div>
    );
};

export default ProjectList;
