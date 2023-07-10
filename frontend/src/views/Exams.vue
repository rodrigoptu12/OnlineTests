<script setup>
    import Navbar from '../components/Navbar.vue';
</script>

<template class="flex">
    <div class="w-full">
        <Navbar />
    </div>

    <div class="flex wrapper">
        <div class="flex mb-6">

            <div class="wrapper-headline w-full">
                <h1 class="mb-1 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
                    Exames.
                </h1>
                <p class="text-lg font-normal text-gray-500 lg:text-l dark:text-gray-400 mb-4">
                    Área de listagem de exames.
                </p>
                <div class="block w-full">
            <button
              type="submit"
              class="text-white bg-blue-700 f hover:bg-blue-800 focus:ring-4 focus:outline-none focus:blue-300 font-medium rounded text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Novo exame
            </button>
        </div>
            </div>
          
        </div>

        <div class="wrapper relative overflow-x-auto border dark:border-blue sm:rounded-l">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:transparent dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">
                            <b>Nome do exame</b>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <b>Criado por</b>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <b>Quantidade de questões</b>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <b>Data</b>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <b><span class="sr-only">Editar</span></b>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        class="bg-transparent border-b dark:bg-transparent dark:border-blue hover:bg-gray-50 dark:hover:bg-gray-600">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Teste 1
                        </th>
                        <td class="px-6 py-4">
                            Eduardo B.
                        </td>
                        <td class="px-6 py-4">
                            08
                        </td>
                        <td class="px-6 py-4">
                            28/04/2023
                        </td>
                        <td class="px-6 py-4 text-right">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a>
                        </td>
                    </tr>
                    <tr
                        class="bg-transparent border-b dark:bg-transparent dark:border-blue hover:bg-gray-50 dark:hover:bg-gray-600">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Teste 2
                        </th>
                        <td class="px-6 py-4">
                            Eduardo B.
                        </td>
                        <td class="px-6 py-4">
                            12
                        </td>
                        <td class="px-6 py-4">
                            03/06/2023
                        </td>
                        <td class="px-6 py-4 text-right">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a>
                        </td>
                    </tr>
                    <tr class="bg-transparent dark:bg-transparent hover:bg-gray-50 dark:hover:bg-gray-600">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Teste 3
                        </th>
                        <td class="px-6 py-4">
                            Eduardo B.
                        </td>
                        <td class="px-6 py-4">
                            10
                        </td>
                        <td class="px-6 py-4">
                            06/07/2023
                        </td>
                        <td class="px-6 py-4 text-right">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

</template>


<style>
    .wrapper {
        left: 0;
        right: 0;
        width: 80vw;
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
        flex-direction: column;
    }

    .wrapper-headline {
        left: 0;
        right: 0;
    }

    #navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        min-width: 100vw;
    }
</style>