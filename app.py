from flask import Flask

app = Flask(__name__)

@app.route("/info")
def myinfo():
    return """
    <h2>My Info</h2>
    <p>Hello! My name is <strong>Himanshu Kumar Singh</strong>.</p>
    <p>I am a DevOps enthusiast currently seeking exciting opportunities in the field of Cloud Infrastructure and Automation.</p>
    <p>I enjoy working on real-world cloud projects and automating deployments using industry-standard DevOps tools.</p>
    """

@app.route("/education")
def myeducation():
    return """
    <h2>My Education</h2>
    <p>I have completed my <strong>Bachelor of Technology (B.Tech)</strong> in <strong>Computer Science and Engineering</strong> 
    from <strong>Jodhpur Institute of Engineering and Technology</strong>.</p>
    <p>Currently, I am pursuing an internship at <strong>LinuxWorld Informatics Pvt. Ltd.</strong>, where I am gaining 
    hands-on experience in various DevOps tools and practices.</p>
    <p>This internship has helped me strengthen my practical skills in areas like:</p>
    <ul>
        <li>CI/CD Pipelines</li>
        <li>Cloud Services (AWS)</li>
        <li>Containerization with Docker</li>
        <li>Container Orchestration using Kubernetes</li>
    </ul>
    """

@app.route("/about")
def about():
    return """
    <h2>About Me</h2>
    <p>Hello! My name is <strong>Himanshu Kumar Singh</strong>. I am a passionate and dedicated DevOps enthusiast, 
    currently completing an internship at <strong>LinuxWorld Informatics Pvt. Ltd.</strong> (LW), where I am gaining hands-on 
    experience in DevOps tools and practices.</p>
    
    <p>I have recently completed my <strong>B.Tech in Computer Science and Engineering</strong> from 
    <strong>Jodhpur Institute of Engineering and Technology</strong>. Throughout my academic journey and internships, I have worked with:</p>
    
    <ul>
        <li><strong>CI/CD Tools:</strong> Jenkins, GitHub Actions, ArgoCD</li>
        <li><strong>Cloud Platforms:</strong> AWS</li>
        <li><strong>Containerization & Orchestration:</strong> Docker, Kubernetes</li>
        <li><strong>Monitoring & Logging:</strong> Prometheus, Grafana, ELK Stack</li>
        <li><strong>Scripting & Automation:</strong> Bash, Ansible</li>
        <li><strong>Version Control:</strong> Git</li>
    </ul>
    
    <p>I’m actively seeking <strong>full-time opportunities in DevOps</strong> where I can contribute to cloud-native infrastructure, 
    automation, and deployment strategies. I love solving real-world problems using scalable and efficient DevOps practices.</p>
    """

if __name__ == "__main__" :
    app.run(host='0.0.0.0', port=5000)

