<script>
    async function getData(url, page, paginateBy) {
        const urlWithParams = url + "?" + new URLSearchParams({
                page: page,
                per_page: paginateBy
            })
        const response = await fetch(urlWithParams);
        return response.json();
    }

    class Paginator {
        constructor(perPage) {
            this.perPage = perPage;
            this.pageIndex = 1;
            this.container = document.getElementById("paginator");
        }
</script>