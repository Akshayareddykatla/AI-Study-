from django.core.management.base import BaseCommand
from quizzes.models import Quiz, Question, Choice

class Command(BaseCommand):
    help = 'Seeds the database with 120+ questions across 10 techs and HR'

    def handle(self, *args, **kwargs):
        content = {
            'Cloud Computing (AWS/Azure)': {
                'cat': 'cloud',
                'questions': [
                    ("What does 'SaaS' stand for?", ["Software as a Service", "System as a Service", "Storage as a Service", "Security as a Service"], 0),
                    ("Which AWS service is used for scalable object storage?", ["S3", "EC2", "RDS", "Lambda"], 0),
                    ("What is a 'Region' in AWS?", ["A physical location with multiple Availability Zones", "A single data center", "A type of database", "A security group"], 0),
                    ("What is the main purpose of Auto Scaling?", ["Adjust capacity to maintain steady performance", "Back up data", "Encrypt traffic", "Manage billing"], 0),
                    ("Which service is a managed NoSQL database in AWS?", ["DynamoDB", "Redshift", "CloudFront", "IAM"], 0),
                    ("What does 'Serverless' mean?", ["Developers don't manage the underlying server infrastructure", "There are no servers involved", "Servers are free", "Servers only run at night"], 0),
                    ("Which Azure service is equivalent to AWS S3?", ["Azure Blob Storage", "Azure Functions", "Azure SQL", "Azure Cosmos DB"], 0),
                    ("What is 'High Availability'?", ["System that is durable and likely to operate continuously", "System that is very fast", "System that costs more", "System with many users"], 0),
                    ("What is VPC in AWS?", ["Virtual Private Cloud", "Virtual Public Cluster", "Version Power Check", "Variable Price Cloud"], 0),
                    ("Which service provides virtual servers in AWS?", ["EC2", "SQS", "SNS", "Route 53"], 0),
                    ("What is CloudFront used for?", ["Content Delivery Network (CDN)", "Database migration", "Machine Learning", "Monitoring"], 0),
                    ("What is the 'Shared Responsibility Model'?", ["Cloud provider manages security 'of' the cloud, user manages security 'in' the cloud", "User pays for half the cloud", "Multiple users share one server", "Developers share code"], 0),
                ]
            },
            'DevOps & Containers (Docker/K8s)': {
                'cat': 'devops',
                'questions': [
                    ("What is a Docker image?", ["A lightweight, standalone, executable package", "A virtual machine", "A text file of code", "A screenshot of an app"], 0),
                    ("Which command is used to build a Docker image?", ["docker build", "docker run", "docker start", "docker push"], 0),
                    ("What is Kubernetes (K8s)?", ["An open-source system for automating container orchestration", "A type of database", "A cloud provider", "A programming language"], 0),
                    ("What is a 'Pod' in Kubernetes?", ["The smallest deployable unit", "A collection of nodes", "A storage disk", "A networking protocol"], 0),
                    ("Which file is used to define Docker images?", ["Dockerfile", "docker-compose.yml", "package.json", "index.html"], 0),
                    ("What is 'CI' in CI/CD?", ["Continuous Integration", "Continuous Injection", "Code Information", "Cloud Instance"], 0),
                    ("What is the purpose of a Load Balancer?", ["Distribute traffic across multiple servers", "Speed up code execution", "Scan for viruses", "Backup data"], 0),
                    ("What is 'Infrastructure as Code' (IaC)?", ["Managing infrastructure using configuration files", "Writing code in the cloud", "Building servers manually", "Coding on hardware"], 0),
                    ("Which tool is popular for IaC?", ["Terraform", "Photoshop", "Excel", "Zoom"], 0),
                    ("What is Grahana used for?", ["Monitoring and visualization", "Database storage", "Code editing", "Video editing"], 0),
                    ("What is a container?", ["Isolated user-space environment", "A physical box for servers", "A heavy virtual machine", "A website folder"], 0),
                    ("What does 'Continuous Deployment' mean?", ["Automatically releasing every code change to production", "Manually checking code", "Writing code daily", "Using a lot of servers"], 0),
                ]
            },
            'Cyber Security': {
                'cat': 'cyber',
                'questions': [
                    ("What does 'HTTPS' stand for?", ["Hypertext Transfer Protocol Secure", "High Text Transfer System", "Hyperlink Total Secure", "Home Technical Security"], 0),
                    ("What is 'Phishing'?", ["Fraudulent attempt to obtain sensitive info via email", "A way to catch fish", "A programming error", "A type of firewall"], 0),
                    ("What is a 'Brute Force' attack?", ["Trying every possible password combination", "Using a physical hammer on a server", "Sending a single large packet", "Stopping a service manually"], 0),
                    ("What is 'Zero Trust' architecture?", ["Always verify every request/user regardless of location", "Never trusting your employees", "Trusting only local users", "Deleting all data every night"], 0),
                    ("What is 'SQL Injection'?", ["Inserting malicious SQL code into input fields", "Optimizing a database", "Deleting a database", "Adding new users"], 0),
                    ("What does 'MFA' stand for?", ["Multi-Factor Authentication", "Most Frequent Access", "Main Frame Admin", "Mobile Filter Application"], 0),
                    ("What is a 'Firewall'?", ["Network security system that monitors traffic", "A physical wall made of fire", "A computer battery", "A type of monitor"], 0),
                    ("What is 'Encryption'?", ["Converting data into a secret code", "Compressing a file", "Deleting history", "Sharing a password"], 0),
                    ("What is the primary goal of CIA Triad?", ["Confidentiality, Integrity, Availability", "Cloud, Internet, Apps", "Centralized, Integrated, Accurate", "Cost, Insurance, Access"], 0),
                    ("What is a 'VPN'?", ["Virtual Private Network", "Variable Price Node", "Virtual Public Network", "Valid Path Note"], 0),
                    ("What is Ransomware?", ["Malware that locks data and demands payment", "Free software", "Software that speeds up PC", "A type of antivirus"], 0),
                    ("What is 'Vulnerability Scanning'?", ["Identifying security weaknesses in a system", "Looking for viruses in images", "Measuring internet speed", "Counting users"], 0),
                ]
            },
            'Data Science & AI': {
                'cat': 'data',
                'questions': [
                    ("What is 'Big Data'?", ["Extremely large data sets analyzed for patterns", "Any file larger than 1GB", "A huge hard drive", "Internet history"], 0),
                    ("Which language is most popular for Data Science?", ["Python", "HTML", "CSS", "PHP"], 0),
                    ("What is 'Supervised Learning'?", ["Training a model on labeled data", "Learning from a teacher", "A robot watching videos", "Coding with a supervisor"], 0),
                    ("What is a 'Neural Network'?", ["A series of algorithms that mimic the human brain", "A group of computers connected by cables", "A type of social media", "A database of neurons"], 0),
                    ("What is 'Pandas' in Python?", ["A library for data manipulation and analysis", "A black and white animal", "A game development tool", "A cloud server"], 0),
                    ("What is 'Overfitting'?", ["Model performs well on training data but poorly on new data", "Model is too small", "Model is perfect", "Model takes too long to run"], 0),
                    ("What is 'NLP'?", ["Natural Language Processing", "New Low Price", "National Logic Path", "Network Level Protocol"], 0),
                    ("What is 'Deep Learning'?", ["A subset of machine learning based on artificial neural networks", "Learning while sleeping", "Studying deep sea data", "Reading many books"], 0),
                    ("Which library is used for Deep Learning?", ["TensorFlow", "Requests", "Flask", "Django"], 0),
                    ("What is a 'Data Warehouse'?", ["Central repository of integrated data for reporting", "A physical building for servers", "A hard drive", "A spreadsheet"], 0),
                    ("What is 'Regression' analysis?", ["Predicting a continuous value", "Grouping similar items", "Deleting outliers", "Finding the max value"], 0),
                    ("What is 'Matplotlib' used for?", ["Data visualization", "Database management", "Web hosting", "Cyber security"], 0),
                ]
            },
            'Freshers HR Interview Questions': {
                'cat': 'hr',
                'questions': [
                    ("How should you answer 'Tell me about yourself'?", ["Focus on education, projects, and career goals", "Tell your life story desde birth", "Talk about your hobbies only", "Ask the interviewer to go first"], 0),
                    ("What is the best way to handle 'What are your weaknesses'?", ["Mention a real weakness and how you are working on it", "Say I am a perfectionist", "Say I have no weaknesses", "Blame your college professor"], 0),
                    ("Why should we hire you?", ["Explain how your skills align with the job requirements", "Because I need a job", "Because I am very smart", "Because I live nearby"], 0),
                    ("What is your salary expectation?", ["Research market rates and give a range if necessary", "Ask for the highest possible", "Say zero", "Ask what they pay others"], 0),
                    ("Where do you see yourself in 5 years?", ["Describe a growth path and desire to learn", "In your seat", "On a beach", "I don't know"], 0),
                    ("How do you handle stress?", ["Talk about time management and staying organized", "I cry", "I quit", "I ignore it"], 0),
                    ("What do you know about our company?", ["Research the company's mission and products", "Nothing", "I saw your logo", "It's a big building"], 0),
                    ("Do you have any questions for us?", ["Ask about team culture or growth opportunities", "When is the next holiday?", "What is the food like?", "No"], 0),
                    ("How do you handle conflict in a team?", ["Discuss communication and finding common ground", "I win the argument", "I leave the team", "I complain to HR"], 0),
                    ("Are you willing to relocate?", ["Be honest about your flexibility", "Yes even if I hate it", "No but say yes", "Depends on the weather"], 0),
                    ("What are your strengths?", ["Mention skills like quick learning and adaptability", "I can sleep 10 hours", "I am rich", "I can eat fast"], 0),
                    ("Why do you want to work here?", ["Show interest in the company's industry and impact", "My parents told me to", "I saw an ad", "Easy commute"], 0),
                ]
            },
            'Web Development (React/Next.js)': {
                'cat': 'web_ai',
                'questions': [
                    ("What is React?", ["A JavaScript library for building user interfaces", "A CSS framework", "A database", "An operating system"], 0),
                    ("What is 'JSX'?", ["Syntax extension for JavaScript", "A Java XML format", "A type of server", "A CSS preprocessor"], 0),
                    ("What are 'Hooks' in React?", ["Functions that let you use state in functional components", "Fishing tools", "CSS selectors", "Database connections"], 0),
                    ("What is Next.js?", ["A React framework with server-side rendering", "A game engine", "A Python library", "A browser"], 0),
                    ("What is 'SSR'?", ["Server-Side Rendering", "Simple Sea Route", "Standard System Rule", "Secure Socket Road"], 0),
                    ("What is 'Virtual DOM'?", ["A programming concept where a virtual representation of UI is kept in memory", "A 3D internet", "A fake website", "Hardware memory"], 0),
                    ("What does 'npm' stand for?", ["Node Package Manager", "New People Meet", "Network Power Management", "Node Private Module"], 0),
                    ("What is 'Tailwind CSS'?", ["A utility-first CSS framework", "A weather app", "A database tool", "A backend language"], 0),
                    ("Which hook is used for side effects in React?", ["useEffect", "useState", "useContext", "useReducer"], 0),
                    ("What is the purpose of 'props' in React?", ["Passing data between components", "Styling elements", "Defining variables", "Deleting items"], 0),
                    ("What is 'Typescript'?", ["A typed superset of JavaScript", "A new font", "A server language", "A script for movies"], 0),
                    ("What is 'DOM'?", ["Document Object Model", "Disk Operating Mode", "Data On Mobile", "Digital Office Mail"], 0),
                ]
            },
            'Blockchain & Web3': {
                'cat': 'blockchain',
                'questions': [
                    ("What is a 'Blockchain'?", ["A distributed, immutable ledger", "A collection of silver chains", "A type of social media", "A fast database"], 0),
                    ("What is 'Smart Contract'?", ["Self-executing contract with terms directly written in code", "A smart person", "A legal document on paper", "A digital signature only"], 0),
                    ("What is 'NFT'?", ["Non-Fungible Token", "New Fast Tech", "Network File Transfer", "Never Find Truth"], 0),
                    ("What is 'Decentralization'?", ["Transfer of control from a central entity to a network", "Moving to the suburbs", "Deleting servers", "Using one big server"], 0),
                    ("Which is the first cryptocurrency?", ["Bitcoin", "Ethereum", "Solana", "Doge"], 0),
                    ("What is a 'Wallet' in Web3?", ["Tool to interact with the blockchain and store keys", "A physical pocket for money", "A folder on a PC", "A bank account"], 0),
                    ("What is 'Gas Fee'?", ["Cost of performing a transaction on Ethereum", "Price of fuel", "Server cooling cost", "Internet bill"], 0),
                    ("What is 'DAO'?", ["Decentralized Autonomous Organization", "Data Access Object", "Digital Art Online", "Direct Access Only"], 0),
                    ("What is 'Mining' in crypto?", ["Process of validating transactions and securing the network", "Digging for gold", "Writing code", "Finding bugs"], 0),
                    ("What is 'Solidity'?", ["Programming language for Ethereum smart contracts", "Being very hard", "A type of database", "A cloud provider"], 0),
                    ("What is 'IPFS'?", ["Distributed system for storing and accessing files", "Internet Protocol for Speed", "Internal Project File System", "Instant Picture Fast Send"], 0),
                    ("What is 'Cold Storage'?", ["Offline storage of crypto assets", "A refrigerator", "Keeping servers in snow", "A slow hard drive"], 0),
                ]
            },
            'IoT & Future Tech': {
                'cat': 'iot',
                'questions': [
                    ("What does 'IoT' stand for?", ["Internet of Things", "Internet of Technology", "Integrated Online Tools", "Internal Object Trace"], 0),
                    ("Which protocol is common in IoT?", ["MQTT", "HTTP", "FTP", "SSH"], 0),
                    ("What is 'Edge Computing'?", ["Processing data closer to the source (device)", "Living on the edge", "Using sharp computers", "Coding at the end of a file"], 0),
                    ("Which device is popular for IoT prototypes?", ["Raspberry Pi", "Apple Watch", "Gaming PC", "Printer"], 0),
                    ("What is '5G'?", ["Fifth Generation mobile network", "5 GB of data", "5 Giga speed", "5 Green servers"], 0),
                    ("What is 'Quantum Computing'?", ["Computing using quantum-mechanical phenomena like superposition", "Very small computers", "Fast gaming computers", "Computers that use water"], 0),
                    ("What is a 'Sensor'?", ["Device that detects changes in the environment", "A security guard", "A type of monitor", "A logic gate"], 0),
                    ("What is 'Augmented Reality' (AR)?", ["Overlaying digital info on the real world", "A fake world in VR", "Better graphics", "High volume"], 0),
                    ("What is 'Li-Fi'?", ["Data transmission using light", "Low-cost Wi-Fi", "Library Fiber", "Long-term internet"], 0),
                    ("What is 'Digital Twin'?", ["Virtual representation of a physical object", "An identical brother", "A second computer", "A copy of a file"], 0),
                    ("What is 'Wearable Tech'?", ["Devices worn on the body", "Clothes with wires", "Computers in bags", "Invisible tech"], 0),
                    ("What is 'Smart City'?", ["City using IoT to improve efficiency and services", "City with smart people", "Small city", "City with robots only"], 0),
                ]
            },
            'Rust Programming & Performance': {
                'cat': 'general',
                'questions': [
                    ("What is the main focus of Rust?", ["Memory safety and performance", "Being easy to learn", "Building websites only", "AI research"], 0),
                    ("What is 'Ownership' in Rust?", ["Unique memory management system to prevent data races", "Owning the source code", "Paying for a license", "Copyright law"], 0),
                    ("Which company created Rust?", ["Mozilla", "Google", "Microsoft", "Apple"], 0),
                    ("What is 'Cargo' in Rust?", ["Package manager and build tool", "A shipping box", "A cloud server", "A variable name"], 0),
                    ("What is 'Zero-cost abstractions'?", ["Features that don't add runtime overhead", "Free software", "Simple code", "No cost cloud"], 0),
                    ("What is 'Immutable' by default in Rust?", ["Variables", "Functions", "Constants only", "Nothing"], 0),
                    ("What is a 'Trait' in Rust?", ["Interface-like functionality", "A bug", "A fast loop", "A data type"], 0),
                    ("What is 'unsafe' block in Rust?", ["Allowing memory-unsafe operations explicitly", "Code that crashes", "Public code", "Old code"], 0),
                    ("Is Rust a compiled or interpreted language?", ["Compiled", "Interpreted", "Both", "Neither"], 0),
                    ("What is 'Borrow Checker'?", ["Enforces ownership rules at compile time", "A tool for loans", "A library for data", "A type of loop"], 0),
                    ("What suffix do Rust files have?", [".rs", ".rust", ".rt", ".ru"], 0),
                    ("Does Rust have a Garbage Collector?", ["No", "Yes", "Optional", "Depends on OS"], 0),
                ]
            },
            'Mobile Development': {
                'cat': 'mobile',
                'questions': [
                    ("What is 'Flutter'?", ["UI toolkit for building natively compiled applications", "A social media app", "A database", "A birds movement"], 0),
                    ("Which language does Flutter use?", ["Dart", "JS", "Swift", "Kotlin"], 0),
                    ("What is 'React Native'?", ["Framework for building native apps using React", "Native JS", "Website on phone", "Android only tool"], 0),
                    ("What is 'Swift'?", ["Language for iOS/macOS apps", "A fast car", "A bank network only", "A CSS framework"], 0),
                    ("What is 'Kotlin'?", ["Primary language for Android development", "A type of coffee", "A cloud server", "A JS library"], 0),
                    ("What is 'PWA'?", ["Progressive Web App", "Public Web Access", "Private Work Area", "Phone Web Application"], 0),
                    ("What is 'App Store Optimization' (ASO)?", ["Improving app visibility in stores", "Making app files smaller", "Coding faster", "Deleting bad reviews"], 0),
                    ("What is 'Firebase'?", ["Backend-as-a-Service for mobile apps", "A fire game", "A database for desktop only", "A physical server"], 0),
                    ("What is 'APK'?", ["Android Package Kit", "Apple Private Key", "Access Point Kernel", "All Power Known"], 0),
                    ("Which component is used for navigation in React Native?", ["React Navigation", "Link tag", "href", "A button"], 0),
                    ("What is 'Hot Reload'?", ["Updating code without restarting the app", "Putting phone in sun", "Fast charging", "Deleting cache"], 0),
                    ("What is 'UI/UX'?", ["User Interface and User Experience", "Universal Internet", "Under Instruction", "Unit X"], 0),
                ]
            }
        }

        total_questions = 0
        for quiz_title, data in content.items():
            quiz, created = Quiz.objects.get_or_create(
                title=quiz_title,
                defaults={'description': f'Test your skills in {quiz_title}.', 'category': data['cat']}
            )
            
            if not created:
                quiz.questions.all().delete() # Refresh questions for existing quizes
                self.stdout.write(f"Refreshing {quiz_title}...")

            for q_text, choices, correct_idx in data['questions']:
                q = Question.objects.create(quiz=quiz, text=q_text)
                for i, c_text in enumerate(choices):
                    Choice.objects.create(
                        question=q,
                        text=c_text,
                        is_correct=(i == correct_idx)
                    )
                total_questions += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(content)} quizzes with {total_questions} questions!'))
