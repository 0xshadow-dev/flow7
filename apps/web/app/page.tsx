import styles from "./page.module.css";

export default function Home() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div className={styles.header}>
          <h1>FLOW7</h1>
        </div>
        
        <div className={styles.content}>
          <p>
            Modern knowledge workers spend 40% of their time on repetitive tasks. 
            The average employee switches between eleven different applications 
            daily, creating constant context switching that fragments attention 
            and reduces cognitive performance.
          </p>
          
          <p>
            While automation tools have proliferated, key gaps remain. The complexity 
            of connecting disparate systems creates friction that prevents teams 
            from achieving meaningful productivity gains. Knowledge of how to 
            orchestrate multi-platform workflows is concentrated within technical 
            teams, limiting both adoption and the broader impact of automation.
          </p>
          
          <p>
            Despite their potential, these systems remain difficult for people 
            to customize to their specific needs and processes. The result is 
            a growing productivity paradox: more tools, more complexity, less 
            actual work accomplished.
          </p>
          
          <p>
            Digital burnout costs businesses $322 billion annually in lost 
            productivity. Teams are drowning in app switching and manual 
            coordination tasks that could be eliminated entirely.
          </p>
        </div>
      </main>
    </div>
  );
}
