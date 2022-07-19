document.getElementById('project-items').addEventListener('click', (event) => {
    let isImgTag = event.target.tagName.toLowerCase() === 'img'
    if (isImgTag) {
        let $projectItem = event.target.closest('.project__item'),
            isSecondClick = $projectItem.classList.contains('active')
        activateOrDeactivateAnImage($projectItem, isSecondClick)
    }
})

function activateOrDeactivateAnImage($item, isSecondClick) {
    if (!isSecondClick) {
        offAllActive()
    }
    $item.classList.toggle('active')
    $item.querySelector('.project__body').classList.toggle('project__body_active')
}

function offAllActive() {
    let $projectItems = document.querySelectorAll('.project__item')
    $projectItems.forEach((item) => {
        item.classList.remove('active')
        item.querySelector('.project__body').classList.remove('project__body_active')
    })
}