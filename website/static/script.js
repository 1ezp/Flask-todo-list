function Addjob(){
    const job = document.getElementById('job').value;
    fetch('/add', {
        method: 'POST',
        body: JSON.stringify({text: job})
    }).then((_res)=> {
        window.location.href='/';
    })}
function Deletejob(jobId){
    fetch('/delete', {
        method: 'POST',
        body: JSON.stringify({id: jobId})
    }).then((_res)=> {
        window.location.href='/';
    })}