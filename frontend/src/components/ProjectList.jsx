import { useEffect, useState } from 'react';
import { fetchProjects } from '../utils/api';  // We will set up this API file soon

const ProjectList = () => {
    const [projects, setProjects] = useState([]);  // State to store projects

    // Fetch projects when component loads
    useEffect(() => {
        const getProjects = async () => {
            const data = await fetchProjects();
            setProjects(data);
        };

        getProjects();
    }, []);  // Empty dependency array to run this effect once on mount

    return (
        <div>
            <h1>Projects</h1>
            <ul>
                {projects.map(project => (
                    <li key={project.id}>{project.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default ProjectList;
