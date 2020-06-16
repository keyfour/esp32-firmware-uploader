<template>
    <div class="container">
        <div class="row align-item-start">
            <div class="col">
                <div class="dropdown">
                    <button class="btn btn-secondary dropdown-toggle" type="button"
                        id="dropdownMenuBoard" data-toggle="dropdown" aria-haspopup="true"
                        aria-expanded="false">
                        Connection port
                    </button>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenuBoard">
                        <a class="dropdown-item" href="#">/dev/ttyUSB0</a>
                        <a class="dropdown-item" href="#">/dev/ttyACM0</a>
                        <a class="dropdown-item" href="#">/dev/ttyS0</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
