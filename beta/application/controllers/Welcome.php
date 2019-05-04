<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Welcome extends CI_Controller {

	public function index()
	{
		$data 								= array();


		if(!empty($_FILES)){
			$full_path 						= $this->do_upload();
			if(!empty($full_path)){
				//echo $full_path;
				$latex 						= $this->getLatex($full_path);
				if(!empty($latex)){
					$data['latex'] 			= $latex;
				}
				else{
					$data['errors'][] 		= "Our algorithms failed to understand your equation!";
				}
			}
			else{
				$data['errors'][] 			= "Error Uploading!";
			}
		}

		//print_r($data);

		$this->load->view('home', $data);
	}

	protected function do_upload(){

		$config['upload_path']          = FCPATH . '/uploads/';
        $config['allowed_types']        = 'gif|jpg|png';
        $config['encrypt_name'] = TRUE;

        $this->load->library('upload', $config);

        if ( ! $this->upload->do_upload('image'))
        {
                $error = array('error' => $this->upload->display_errors());

                return false;
        }
        else
        {
                $data = array('upload_data' => $this->upload->data());

                return $data['upload_data']['full_path'];
        }
	}

	protected function getLatex($full_path){

		$url = "http://127.0.0.1:5000/latexer?image=" . $full_path;
		

		$ch = curl_init();		 
		curl_setopt($ch, CURLOPT_URL, $url);		 
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);		 
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);		 
		$data = curl_exec($ch);
		curl_close($ch);
		 
		$data = json_decode($data);
		if(isset($data->latex)){
			return $data->latex;
		}
		else{
			return false;
		}
	}
}
