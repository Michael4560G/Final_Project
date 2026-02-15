document.addEventListener('DOMContentLoaded', async () => {
    // 1. חילוץ מספר הרכב מה-URL
    const urlParams = new URLSearchParams(window.location.search);
    const plate = urlParams.get('plate');

    if (!plate) {
        alert("לא הוזן מספר רכב");
        window.location.href = 'search.html';
        return;
    }

    try {
        // 2. קריאה ל-API של פרטי הרכב
        const carResId = '053cea08-09bc-40ec-8f7a-156f0677aff3';
        const carUrl = `https://data.gov.il/api/3/action/datastore_search?resource_id=${carResId}&q=${plate}`;
        
        const carResponse = await fetch(carUrl);
        const carData = await carResponse.json();

        if (carData.success && carData.result.records.length > 0) {
            const car = carData.result.records[0];
            
            // מילוי השדות בדף
            document.getElementById('res_plate').value = car.mispar_rechev;
            document.getElementById('res_make').value = car.tozeret_nm;
            document.getElementById('res_model').value = car.degem_nm;
            document.getElementById('res_year').value = car.shnat_yitzur;
            document.getElementById('res_color').value = car.tzeva_rechev;
            document.getElementById('res_fuel').value = car.sug_delek_nm;
            document.getElementById('res_test').value = car.mivchan_acharon_dt;
            document.getElementById('res_license').value = car.tokef_dt;
            document.getElementById('res_pollution').value = car.kvutzat_zihum;
            document.getElementById('res_tire_f').value = car.zmig_kidmi;
            document.getElementById('res_tire_r').value = car.zmig_ahori;
        } else {
            alert("רכב לא נמצא במאגר");
        }

        // 3. בדיקת תו נכה
        const tagResId = 'c8b9f9c8-4612-4068-934f-d4acd2e3c06e';
        const tagUrl = `https://data.gov.il/api/3/action/datastore_search?resource_id=${tagResId}&q=${plate}`;
        
        const tagResponse = await fetch(tagUrl);
        const tagData = await tagResponse.json();
        const hasTag = tagData.result.records.length > 0;

        const tagBox = document.getElementById('disabledTagBox');
        const tagText = document.getElementById('tagText');

        if (hasTag) {
            tagBox.classList.add('has-tag');
            tagText.innerText = "♿ לרכב זה יש תו נכה פעיל במאגר";
        } else {
            tagBox.classList.add('no-tag');
            tagText.innerText = "לרכב זה אין תו נכה במאגר";
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        alert("אירעה שגיאה בחיבור למאגרי הממשלה");
    } finally {
        // הסרת מסך הטעינה
        document.getElementById('loading').style.display = 'none';
    }
});