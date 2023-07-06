# model_simulator
for simulating models built

cd ../../users/sylvanus jerome/documents/python_scripts/models_simulator
cd Documents/things-n-thingses/python/web-stack/models_simulator

{% for case in object_list %}
<tr role="row" class="odd">
<td class="">{{ forloop.counter }}</td>
    {% if case.sentence == 'Not Sentence' %}

    <td class="text-success">{{ case.text}}</td>
    <td class="text-success">{{ case.sentence}}</td>
    <td class="text-success">{{ case.crime }}</td>
    {% else %}
    <td class="text-danger">{{ case.text}}</td>
    <td class="text-danger">{{ case.sentence}}</td>
    <td class="text-danger">{{ case.crime }}</td>
    {% endif %}

    <td>
        <a href="#" class="btn btn-primary disabled"><i class="fa fa-edit" title="View Result"></i>
        </a>

    </td>
</tr>
{% endfor %}