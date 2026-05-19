var button = document.getElementsByClassName("Mark-button")
var delete_button = document.getElementsByClassName("delete-button")

for (var i = 0; i < button.length; i++)
{
    button[i].onchange = (e)=>{

        var check_box = e.target
        var task_id = check_box.value
        var is_completed = check_box.checked
        var update_task_url = "/update-task/"
        var task_box = check_box.parentElement.parentElement
        var status_text = task_box.getElementsByClassName("status-text")[0]

        fetch(update_task_url,{
            "method" : "PUT",
            "body" : JSON.stringify({
                "task_id" : task_id,
                "is_completed" : is_completed
            })
        }).then(r=>r.json()).then(res=>{

            console.log(res)

            if(res.status == true){

                if(is_completed == true){
                    task_box.className = "completed"
                    check_box.checked = true
                    status_text.innerHTML = "Completed"
                }
                else{
                    task_box.className = "pending"
                    check_box.checked = false
                    status_text.innerHTML = "Pending"
                }

            }

        })
    }
}

for (var j = 0; j < delete_button.length; j++)
{
    delete_button[j].onclick = (e)=>{

        var delete_btn = e.target
        var task_id = delete_btn.value
        var delete_task_url = "/delete-task/"
        var task_card = delete_btn.parentElement.parentElement.parentElement

        var confirm_delete = confirm("Do you want to delete this task?")

        if(confirm_delete == true){
            fetch(delete_task_url,{
                "method" : "DELETE",
                "body" : JSON.stringify({
                    "task_id" : task_id
                })
            }).then(r=>r.json()).then(res=>{

                console.log(res)

                if(res.status == true){
                    task_card.remove()
                }

            })
        }
    }
}
