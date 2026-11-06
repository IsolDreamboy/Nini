import { useState, useEffect } from 'react';

// Tipagem da resposta retornada pelo FastAPI
interface ResultadoNini {
  paciente_id: string;
  status: string;
  triage_result: {
    manchester_cor: string;
    pontuacao_de_risco: number;
    resumo_clinico: string;
    acao_recomendada: string;
  };
}

export const ComponenteTriagem = () => {
  const [carregando, setCarregando] = useState(false);
  const [resultado, setResultado] = useState<ResultadoNini | null>(null);
  const [erro, setErro] = useState<string | null>(null);

  // Estado zerado para preenchimento manual real com TODOS os campos do backend
  const [dadosFormulario, setDadosFormulario] = useState({
    registro: {
      nome_completo: "",
      nome_social: "",
      cpf: "",
      rg: "",
      data_de_nascimento: "",
      sexo_biologico: "Masculino",
      etnia: "Não Informada",
      email: "",
      telefone: "",
      cep: "",
      complemento_cep: "",
      regiao: "Sul",
      uf: "PR",
      municipio: "",
      historico_de_deslocamento: "Nenhum"
    },
    triagem: {
      alergias: [] as string[],
      diabetes: false,
      doencas_geneticas: "Nenhuma",
      historico_familiar: "Nenhum",
      historico_clinico_geral: "Sem comorbidades prévias",
      medicamento_em_uso: [] as string[],
      cirurgia_previas: [] as string[],
      status_vacinal: "Em dia",
      grupo_de_risco: false,
      historico_de_viagens_recente: "Nenhuma"
    },
    antropometria: {
      peso: 70.0,
      altura: 1.75,
      imc: 24.2,
      tipo_sanguineo: "O",
      fator_rh: "+"
    },
    estilo_de_vida: {
      fumante: false,
      alcoolico: false,
      atividades_fisicas: "Nenhuma",
      habitos_alimentares: "Regulares",
      dados_demograficos: "Urbano",
      ocupacao_profissional: "Não informada"
    },
    sinais_vitais: {
      frequencia_cardiaca: 80,
      pressao_arterial: "120/80",
      saturacao_de_oxigenio: 98,
      temperatura_corporal: 36.5,
      glicemia: 90
    },
    sintomas: {
      sintomas: [] as string[]
    }
  });

 
  const [sintomasInput, setSintomasInput] = useState("");
  const [alergiasInput, setAlergiasInput] = useState("");
  const [medicamentosInput, setMedicamentosInput] = useState("");
  const [cirurgiasInput, setCirurgiasInput] = useState("");

  
  useEffect(() => {
    if (dadosFormulario.antropometria.peso > 0 && dadosFormulario.antropometria.altura > 0) {
      const imcCalc = dadosFormulario.antropometria.peso / (dadosFormulario.antropometria.altura * dadosFormulario.antropometria.altura);
      setDadosFormulario(prev => ({
        ...prev,
        antropometria: { ...prev.antropometria, imc: parseFloat(imcCalc.toFixed(2)) }
      }));
    }
  }, [dadosFormulario.antropometria.peso, dadosFormulario.antropometria.altura]);

  const submeterProntuario = async (e: React.FormEvent) => {
    e.preventDefault();
    setCarregando(true);
    setResultado(null);
    setErro(null);

    // Converte os textos com vírgula para arrays reais e formata os dados
    const payloadFormatado = {
      ...dadosFormulario,
      registro: {
        ...dadosFormulario.registro,
        email: dadosFormulario.registro.email.trim() || "paciente@exemplo.com"
      },
      sintomas: {
        sintomas: sintomasInput.split(',').map(s => s.trim()).filter(Boolean)
      },
      triagem: {
        ...dadosFormulario.triagem,
        alergias: alergiasInput.split(',').map(a => a.trim()).filter(Boolean),
        medicamento_em_uso: medicamentosInput.split(',').map(m => m.trim()).filter(Boolean),
        cirurgia_previas: cirurgiasInput.split(',').map(c => c.trim()).filter(Boolean)
      }
    };

    try {
      const response = await fetch('http://localhost:8019/api/v1/triagem/processar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payloadFormatado),
      });

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.detail || 'Erro ao processar a triagem no backend.');
      }

      const data: ResultadoNini = await response.json();
      setResultado(data);
    } catch (err: any) {
      setErro(err.message || 'Erro de conexão com o servidor.');
    } finally {
      setCarregando(false);
    }
  };

  const getCorBadge = (cor: string) => {
    switch (cor?.toLowerCase()) {
      case 'vermelho': return 'bg-red-600 text-white';
      case 'laranja': return 'bg-orange-500 text-white';
      case 'amarelo': return 'bg-yellow-400 text-gray-900';
      case 'verde': return 'bg-green-600 text-white';
      case 'azul': return 'bg-blue-600 text-white';
      default: return 'bg-gray-600 text-white';
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6 flex flex-col items-center">
      <div className="max-w-6xl w-full bg-white rounded-xl shadow-lg p-8 space-y-6">
        <header className="border-b pb-4 flex justify-between items-end">
          <div>
            <h1 className="text-3xl font-bold text-gray-800">Prontuário de Triagem Médica — Nini AI</h1>
            <p className="text-sm text-gray-500 mt-1">Preencha todos os parâmetros clínicos para análise do LangGraph.</p>
          </div>
        </header>

        <form onSubmit={submeterProntuario} className="space-y-6">
          {/* SEÇÃO 1: IDENTIFICAÇÃO E DEMOGRAFIA */}
          <div className="bg-gray-50 p-5 rounded-lg border border-gray-200">
            <h2 className="text-lg font-semibold text-gray-700 mb-4 border-b pb-2">1. Dados de Identificação (Registro)</h2>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4 text-sm">
              <div className="md:col-span-2">
                <label className="block text-gray-600 font-medium">Nome Completo</label>
                <input type="text" required value={dadosFormulario.registro.nome_completo} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, nome_completo: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div className="md:col-span-2">
                <label className="block text-gray-600 font-medium">Nome Social</label>
                <input type="text" value={dadosFormulario.registro.nome_social} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, nome_social: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              
              <div>
                <label className="block text-gray-600 font-medium">CPF</label>
                <input type="text" required value={dadosFormulario.registro.cpf} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, cpf: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">RG</label>
                <input type="text" required value={dadosFormulario.registro.rg} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, rg: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Data de Nascimento</label>
                <input type="date" required value={dadosFormulario.registro.data_de_nascimento} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, data_de_nascimento: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Etnia</label>
                <select value={dadosFormulario.registro.etnia} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, etnia: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1">
                  <option value="Não Informada">Não Informada</option>
                  <option value="Branca">Branca</option>
                  <option value="Preta">Preta</option>
                  <option value="Parda">Parda</option>
                  <option value="Amarela">Amarela</option>
                  <option value="Indígena">Indígena</option>
                </select>
              </div>

              <div>
                <label className="block text-gray-600 font-medium">Sexo Biológico</label>
                <select value={dadosFormulario.registro.sexo_biologico} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, sexo_biologico: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1">
                  <option value="Masculino">Masculino</option>
                  <option value="Feminino">Feminino</option>
                </select>
              </div>
              <div className="md:col-span-2">
                <label className="block text-gray-600 font-medium">E-mail</label>
                <input type="email" value={dadosFormulario.registro.email} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, email: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Telefone</label>
                <input type="text" value={dadosFormulario.registro.telefone} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, telefone: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              
              <div>
                <label className="block text-gray-600 font-medium">CEP</label>
                <input type="text" value={dadosFormulario.registro.cep} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, cep: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">UF</label>
                <input type="text" value={dadosFormulario.registro.uf} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, uf: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Município</label>
                <input type="text" value={dadosFormulario.registro.municipio} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, municipio: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Região</label>
                <select value={dadosFormulario.registro.regiao} onChange={(e) => setDadosFormulario({ ...dadosFormulario, registro: { ...dadosFormulario.registro, regiao: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1">
                  <option value="Sul">Sul</option>
                  <option value="Sudeste">Sudeste</option>
                  <option value="Centro-Oeste">Centro-Oeste</option>
                  <option value="Nordeste">Nordeste</option>
                  <option value="Norte">Norte</option>
                </select>
              </div>
            </div>
          </div>

          {/* SEÇÃO 2: ANTROPOMETRIA */}
          <div className="bg-gray-50 p-5 rounded-lg border border-gray-200">
            <h2 className="text-lg font-semibold text-gray-700 mb-4 border-b pb-2">2. Antropometria</h2>
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4 text-sm">
              <div>
                <label className="block text-gray-600 font-medium">Peso (kg)</label>
                <input type="number" step="0.1" required value={dadosFormulario.antropometria.peso} onChange={(e) => setDadosFormulario({ ...dadosFormulario, antropometria: { ...dadosFormulario.antropometria, peso: parseFloat(e.target.value) } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Altura (m)</label>
                <input type="number" step="0.01" required value={dadosFormulario.antropometria.altura} onChange={(e) => setDadosFormulario({ ...dadosFormulario, antropometria: { ...dadosFormulario.antropometria, altura: parseFloat(e.target.value) } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">IMC (Auto)</label>
                <input type="number" readOnly value={dadosFormulario.antropometria.imc} className="w-full border rounded-lg p-2.5 mt-1 bg-gray-200" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Tipo Sanguíneo</label>
                <select value={dadosFormulario.antropometria.tipo_sanguineo} onChange={(e) => setDadosFormulario({ ...dadosFormulario, antropometria: { ...dadosFormulario.antropometria, tipo_sanguineo: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1">
                  <option value="O">O</option>
                  <option value="A">A</option>
                  <option value="B">B</option>
                  <option value="AB">AB</option>
                </select>
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Fator RH</label>
                <select value={dadosFormulario.antropometria.fator_rh} onChange={(e) => setDadosFormulario({ ...dadosFormulario, antropometria: { ...dadosFormulario.antropometria, fator_rh: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1">
                  <option value="+">Positivo (+)</option>
                  <option value="-">Negativo (-)</option>
                </select>
              </div>
            </div>
          </div>

          {/* SEÇÃO 3: ESTILO DE VIDA */}
          <div className="bg-gray-50 p-5 rounded-lg border border-gray-200">
            <h2 className="text-lg font-semibold text-gray-700 mb-4 border-b pb-2">3. Estilo de Vida</h2>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4 text-sm items-center">
              <div className="flex items-center space-x-2">
                <input type="checkbox" checked={dadosFormulario.estilo_de_vida.fumante} onChange={(e) => setDadosFormulario({ ...dadosFormulario, estilo_de_vida: { ...dadosFormulario.estilo_de_vida, fumante: e.target.checked } })} className="w-5 h-5" />
                <label className="text-gray-700 font-medium">Paciente Fumante</label>
              </div>
              <div className="flex items-center space-x-2">
                <input type="checkbox" checked={dadosFormulario.estilo_de_vida.alcoolico} onChange={(e) => setDadosFormulario({ ...dadosFormulario, estilo_de_vida: { ...dadosFormulario.estilo_de_vida, alcoolico: e.target.checked } })} className="w-5 h-5" />
                <label className="text-gray-700 font-medium">Consumo Alcoólico</label>
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Atividades Físicas</label>
                <input type="text" value={dadosFormulario.estilo_de_vida.atividades_fisicas} onChange={(e) => setDadosFormulario({ ...dadosFormulario, estilo_de_vida: { ...dadosFormulario.estilo_de_vida, atividades_fisicas: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Ocupação / Profissão</label>
                <input type="text" value={dadosFormulario.estilo_de_vida.ocupacao_profissional} onChange={(e) => setDadosFormulario({ ...dadosFormulario, estilo_de_vida: { ...dadosFormulario.estilo_de_vida, ocupacao_profissional: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
            </div>
          </div>

          {/* SEÇÃO 4: HISTÓRICO CLÍNICO E TRIAGEM */}
          <div className="bg-gray-50 p-5 rounded-lg border border-gray-200">
            <h2 className="text-lg font-semibold text-gray-700 mb-4 border-b pb-2">4. Histórico Clínico Geral</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
              <div className="flex space-x-6 mb-2">
                <div className="flex items-center space-x-2">
                  <input type="checkbox" checked={dadosFormulario.triagem.diabetes} onChange={(e) => setDadosFormulario({ ...dadosFormulario, triagem: { ...dadosFormulario.triagem, diabetes: e.target.checked } })} className="w-5 h-5" />
                  <label className="text-red-700 font-bold">Portador de Diabetes</label>
                </div>
                <div className="flex items-center space-x-2">
                  <input type="checkbox" checked={dadosFormulario.triagem.grupo_de_risco} onChange={(e) => setDadosFormulario({ ...dadosFormulario, triagem: { ...dadosFormulario.triagem, grupo_de_risco: e.target.checked } })} className="w-5 h-5" />
                  <label className="text-red-700 font-bold">Grupo de Risco</label>
                </div>
              </div>
              <div></div> {/* Espaçador */}

              <div>
                <label className="block text-gray-600 font-medium">Histórico Familiar</label>
                <input type="text" value={dadosFormulario.triagem.historico_familiar} onChange={(e) => setDadosFormulario({ ...dadosFormulario, triagem: { ...dadosFormulario.triagem, historico_familiar: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Doenças Genéticas</label>
                <input type="text" value={dadosFormulario.triagem.doencas_geneticas} onChange={(e) => setDadosFormulario({ ...dadosFormulario, triagem: { ...dadosFormulario.triagem, doencas_geneticas: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div className="md:col-span-2">
                <label className="block text-gray-600 font-medium">Histórico Clínico Geral</label>
                <textarea value={dadosFormulario.triagem.historico_clinico_geral} onChange={(e) => setDadosFormulario({ ...dadosFormulario, triagem: { ...dadosFormulario.triagem, historico_clinico_geral: e.target.value } })} className="w-full border rounded-lg p-2.5 mt-1 h-16"></textarea>
              </div>
              
              <div>
                <label className="block text-gray-600 font-medium">Medicamentos em Uso (separar por vírgula)</label>
                <input type="text" value={medicamentosInput} onChange={(e) => setMedicamentosInput(e.target.value)} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-gray-600 font-medium">Cirurgias Prévias (separar por vírgula)</label>
                <input type="text" value={cirurgiasInput} onChange={(e) => setCirurgiasInput(e.target.value)} className="w-full border rounded-lg p-2.5 mt-1" />
              </div>
            </div>
          </div>

          {/* SEÇÃO 5: SINAIS VITAIS */}
          <div className="bg-blue-50 p-5 rounded-lg border border-blue-200">
            <h2 className="text-lg font-semibold text-blue-800 mb-4 border-b border-blue-200 pb-2">5. Sinais Vitais (Atendimento)</h2>
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4 text-sm">
              <div>
                <label className="block text-blue-900 font-medium">Pressão Arterial</label>
                <input type="text" required value={dadosFormulario.sinais_vitais.pressao_arterial} onChange={(e) => setDadosFormulario({ ...dadosFormulario, sinais_vitais: { ...dadosFormulario.sinais_vitais, pressao_arterial: e.target.value } })} className="w-full border-blue-300 rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-blue-900 font-medium">Temp. (°C)</label>
                <input type="number" step="0.1" required value={dadosFormulario.sinais_vitais.temperatura_corporal} onChange={(e) => setDadosFormulario({ ...dadosFormulario, sinais_vitais: { ...dadosFormulario.sinais_vitais, temperatura_corporal: parseFloat(e.target.value) } })} className="w-full border-blue-300 rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-blue-900 font-medium">Sat. O2 (%)</label>
                <input type="number" required value={dadosFormulario.sinais_vitais.saturacao_de_oxigenio} onChange={(e) => setDadosFormulario({ ...dadosFormulario, sinais_vitais: { ...dadosFormulario.sinais_vitais, saturacao_de_oxigenio: parseInt(e.target.value) } })} className="w-full border-blue-300 rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-blue-900 font-medium">Freq. Cardíaca</label>
                <input type="number" required value={dadosFormulario.sinais_vitais.frequencia_cardiaca} onChange={(e) => setDadosFormulario({ ...dadosFormulario, sinais_vitais: { ...dadosFormulario.sinais_vitais, frequencia_cardiaca: parseInt(e.target.value) } })} className="w-full border-blue-300 rounded-lg p-2.5 mt-1" />
              </div>
              <div>
                <label className="block text-blue-900 font-medium">Glicemia (mg/dL)</label>
                <input type="number" required value={dadosFormulario.sinais_vitais.glicemia} onChange={(e) => setDadosFormulario({ ...dadosFormulario, sinais_vitais: { ...dadosFormulario.sinais_vitais, glicemia: parseInt(e.target.value) } })} className="w-full border-blue-300 rounded-lg p-2.5 mt-1" />
              </div>
            </div>
          </div>

          {/* SEÇÃO 6: SINTOMAS */}
          <div className="bg-red-50 p-5 rounded-lg border border-red-200">
            <h2 className="text-lg font-semibold text-red-800 mb-4 border-b border-red-200 pb-2">6. Motivo do Atendimento</h2>
            <div className="space-y-4 text-sm">
              <div>
                <label className="block text-red-900 font-bold">Sintomas e Queixas Principais (separados por vírgula)</label>
                <input type="text" required placeholder="Ex: Dor no peito intensa, Falta de ar, Sudorese" value={sintomasInput} onChange={(e) => setSintomasInput(e.target.value)} className="w-full border-red-300 rounded-lg p-3 mt-1 text-red-900 font-medium focus:ring-2 focus:ring-red-500 outline-none" />
              </div>
              <div>
                <label className="block text-red-900 font-medium">Alergias Conhecidas (separadas por vírgula)</label>
                <input type="text" placeholder="Ex: Penicilina, Dipirona, Iodo" value={alergiasInput} onChange={(e) => setAlergiasInput(e.target.value)} className="w-full border-red-300 rounded-lg p-2.5 mt-1" />
              </div>
            </div>
          </div>

          <button type="submit" disabled={carregando} className="w-full py-4 bg-blue-700 hover:bg-blue-800 text-white font-bold text-xl rounded-xl shadow-lg transition disabled:opacity-50">
            {carregando ? 'Nini processando raciocínio clínico e IA...' : 'Executar Triagem Médica Final'}
          </button>
        </form>

        {erro && (
          <div className="p-4 bg-red-100 border-l-4 border-red-600 text-red-800 rounded-md mt-4 text-sm">
            <strong>Erro na requisição:</strong> {erro}
          </div>
        )}

        {/* RESULTADO DA NINI */}
        {resultado && (
          <div className="mt-8 p-6 rounded-2xl border-2 border-gray-200 bg-white shadow-2xl space-y-5 transform animate-fade-in-up">
            <div className="flex items-center justify-between border-b pb-4">
              <div>
                <h3 className="text-2xl font-black text-gray-800 uppercase tracking-tight">Parecer Diagnóstico — Nini</h3>
                <p className="text-xs text-gray-400 mt-1 font-mono">Prontuário UUID: {resultado.paciente_id}</p>
              </div>
              <span className={`px-6 py-2.5 text-lg font-black rounded-xl uppercase tracking-wider ${getCorBadge(resultado.triage_result.manchester_cor)}`}>
                Manchester: {resultado.triage_result.manchester_cor}
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-gray-50 p-5 rounded-xl border border-gray-200">
                <strong className="text-gray-800 text-sm uppercase tracking-wider flex items-center mb-2">
                   Resumo Clínico
                </strong>
                <p className="text-gray-700 text-sm leading-relaxed">
                  {resultado.triage_result.resumo_clinico}
                </p>
              </div>

              <div className="bg-blue-50 p-5 rounded-xl border border-blue-200">
                <strong className="text-blue-900 text-sm uppercase tracking-wider flex items-center mb-2">
                   Conduta Recomendada
                </strong>
                <p className="text-blue-800 text-sm leading-relaxed font-medium">
                  {resultado.triage_result.acao_recomendada}
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ComponenteTriagem;